import os
import sys
import re
import uuid
import hashlib
import yaml
import builtins
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Настройка безопасного вывода в консоль для предотвращения UnicodeEncodeError на Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def safe_print(*args, **kwargs):
    file = kwargs.get('file', sys.stdout)
    enc = getattr(file, 'encoding', 'utf-8') or 'utf-8'
    new_args = []
    for a in args:
        if isinstance(a, str):
            new_args.append(a.encode(enc, errors='replace').decode(enc))
        else:
            new_args.append(a)
    builtins.print(*new_args, **kwargs)

print = safe_print

from src.database import MemoryDatabase
from src.config import BASE_DIR

# Директории для сканирования (относительно AGrav root)
AGRAV_ROOT = BASE_DIR.parent.parent # d:\works\AGrav
FOLDERS_TO_SCAN = [
    "00_Система",
    "10_Работа",
    "10_Теория_и_Методы",
    "15_Дом",
    "20_Проекты",
    "30_Библиотека"
]

EXCLUDE_DIRS = {
    "cach",
    "temp",
    "scratch",
    "MemoryDB",  # Исключаем сам проект базы данных
    ".git",
    ".obsidian"
}

class VaultIndexer:
    def __init__(self, db: MemoryDatabase):
        self.db = db
        self.root_path = Path(AGRAV_ROOT).resolve()

    def get_project_context(self, file_path: Path) -> str:
        """Определяет проектный контекст на основе пути к файлу."""
        relative_path = file_path.relative_to(self.root_path)
        parts = relative_path.parts
        
        if not parts:
            return "global"
            
        first_dir = parts[0]
        if first_dir == "20_Проекты" and len(parts) > 1:
            return parts[1]
        elif first_dir == "10_Работа" and len(parts) > 1:
            return parts[1]
        elif first_dir == "15_Дом" and len(parts) > 1:
            return parts[1]
            
        return first_dir

    def calculate_hash(self, text: str) -> str:
        """Вычисляет MD5-хэш текста."""
        return hashlib.md5(text.encode("utf-8", errors="ignore")).hexdigest()

    def parse_markdown_file(self, file_path: Path) -> Tuple[Dict[str, Any], str, str]:
        """Парсит markdown файл, извлекая frontmatter и остальное содержимое."""
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        frontmatter = {}
        markdown_content = content

        # Регулярное выражение для поиска YAML frontmatter в начале файла
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            yaml_block = match.group(1)
            markdown_content = content[match.end():]
            try:
                frontmatter = yaml.safe_load(yaml_block) or {}
            except Exception as e:
                import sys
                print(f"[Предупреждение] Ошибка парсинга frontmatter в {file_path}: {e}", file=sys.stderr)

        return frontmatter, markdown_content, content

    def update_file_frontmatter(self, file_path: Path, frontmatter: Dict[str, Any], markdown_content: str, original_content: str):
        """Безопасно записывает обновленный frontmatter обратно в файл, сохраняя переносы строк."""
        # Сериализуем frontmatter
        yaml_block = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
        line_ending = "\r\n" if "\r\n" in original_content else "\n"
        
        new_content = f"---{line_ending}{yaml_block}{line_ending}---{line_ending}{markdown_content}"
        
        # Перезаписываем файл
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.write(new_content)

    def chunk_markdown(self, content: str, max_chunk_chars: int = 3000) -> List[Dict[str, str]]:
        """Разбивает текст заметки на логические чанки по markdown-заголовкам."""
        lines = content.splitlines()
        raw_chunks = []
        current_header = "Введение"
        current_chunk_lines = []

        for line in lines:
            # Ищем заголовки Markdown (# , ## , ### и т.д.)
            match = re.match(r"^(#{1,6})\s+(.*)$", line)
            if match:
                if current_chunk_lines:
                    raw_chunks.append({
                        "heading": current_header,
                        "text": "\n".join(current_chunk_lines).strip()
                    })
                current_header = match.group(2).strip()
                current_chunk_lines = [line]
            else:
                current_chunk_lines.append(line)

        if current_chunk_lines:
            raw_chunks.append({
                "heading": current_header,
                "text": "\n".join(current_chunk_lines).strip()
            })

        # Дробление слишком больших чанков по параграфам
        final_chunks = []
        for rc in raw_chunks:
            text = rc["text"]
            if len(text) <= max_chunk_chars:
                final_chunks.append(rc)
            else:
                paragraphs = text.split("\n\n")
                sub_chunk_lines = []
                sub_idx = 1
                for p in paragraphs:
                    # Оцениваем размер при добавлении параграфа
                    current_len = sum(len(x) + 2 for x in sub_chunk_lines) + len(p)
                    if current_len > max_chunk_chars:
                        if sub_chunk_lines:
                            final_chunks.append({
                                "heading": f"{rc['heading']} (часть {sub_idx})",
                                "text": "\n\n".join(sub_chunk_lines).strip()
                            })
                            sub_idx += 1
                        sub_chunk_lines = [p]
                    else:
                        sub_chunk_lines.append(p)
                if sub_chunk_lines:
                    final_chunks.append({
                        "heading": f"{rc['heading']} (часть {sub_idx})",
                        "text": "\n\n".join(sub_chunk_lines).strip()
                    })

        return final_chunks

    def sync(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Сканирует хранилище AGrav, сверяет хэши и обновляет базу Qdrant.
        Удаляет из базы чанки для удаленных файлов.
        """
        print("=== Старт синхронизации базы знаний с Qdrant ===")
        
        # 1. Получаем все memory_id, которые сейчас проиндексированы в Qdrant
        indexed_memories = self.db.get_all_indexed_memory_ids()
        print(f"Всего заметок в индексе Qdrant: {len(set(indexed_memories.keys()))}")

        found_files = []
        updated_count = 0
        created_count = 0
        skipped_count = 0
        active_memory_ids = set()

        # 2. Сканируем директории
        for folder in FOLDERS_TO_SCAN:
            folder_path = self.root_path / folder
            if not folder_path.exists():
                continue
                
            for root, dirs, files in os.walk(folder_path):
                # Исключаем служебные папки
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                
                for file in files:
                    if file.endswith(".md"):
                        found_files.append(Path(root) / file)

        print(f"Найдено Markdown-файлов для проверки: {len(found_files)}")

        # 3. Обрабатываем каждый файл
        for file_path in found_files:
            try:
                frontmatter, markdown_content, original_content = self.parse_markdown_file(file_path)
                
                # Считаем хэш контента (без учета frontmatter)
                content_hash = self.calculate_hash(markdown_content)
                
                memory_id = frontmatter.get("memory_id")
                old_hash = frontmatter.get("hash")
                
                # Файл изменен или новый
                need_reindex = False
                is_new = False
                
                if not memory_id:
                    memory_id = str(uuid.uuid4())
                    need_reindex = True
                    is_new = True
                elif old_hash != content_hash:
                    need_reindex = True
                
                active_memory_ids.add(memory_id)
                
                if need_reindex:
                    if dry_run:
                        print(f"[Dry Run] Требует индексации: {file_path.relative_to(self.root_path)}")
                        if is_new:
                            created_count += 1
                        else:
                            updated_count += 1
                        continue

                    project_context = self.get_project_context(file_path)
                    
                    # Нарезаем на чанки
                    chunks = self.chunk_markdown(markdown_content)
                    for c in chunks:
                        c["project_context"] = project_context
                        
                    # Сохраняем в Qdrant
                    relative_path_str = str(file_path.relative_to(self.root_path)).replace("\\", "/")
                    success = self.db.save_note_chunks(
                        memory_id=memory_id,
                        file_path=relative_path_str,
                        content_hash=content_hash,
                        chunks=chunks
                    )
                    
                    if success:
                        # Обновляем frontmatter в файле
                        frontmatter["memory_id"] = memory_id
                        frontmatter["hash"] = content_hash
                        frontmatter["last_indexed"] = datetime.utcnow().isoformat()
                        
                        self.update_file_frontmatter(file_path, frontmatter, markdown_content, original_content)
                        
                        if is_new:
                            print(f"[NEW] Проиндексирован файл: {relative_path_str} ({len(chunks)} чанков)")
                            created_count += 1
                        else:
                            print(f"[MODIFIED] Переиндексирован файл: {relative_path_str} ({len(chunks)} чанков)")
                            updated_count += 1
                    else:
                        print(f"[ОШИБКА] Не удалось проиндексировать {relative_path_str}")
                else:
                    skipped_count += 1
            except Exception as e:
                import traceback
                print(f"[ОШИБКА] Сбой при обработке {file_path}: {e}")
                traceback.print_exc()

        # 4. Удаляем из Qdrant записи для файлов, которые больше не существуют на диске
        deleted_count = 0
        for mid, relative_path in indexed_memories.items():
            if mid not in active_memory_ids:
                if dry_run:
                    print(f"[Dry Run] Будет удален из индекса: {relative_path} (ID: {mid})")
                    deleted_count += 1
                    continue
                    
                print(f"[DELETE] Удаление устаревшего индекса для: {relative_path} (ID: {mid})")
                self.db.delete_note_chunks(mid)
                deleted_count += 1

        print(f"Синхронизация завершена. Создано: {created_count}, Обновлено: {updated_count}, Пропущено: {skipped_count}, Удалено из индекса: {deleted_count}")
        return {
            "created": created_count,
            "updated": updated_count,
            "skipped": skipped_count,
            "deleted": deleted_count
        }

if __name__ == "__main__":
    db = MemoryDatabase()
    indexer = VaultIndexer(db)
    indexer.sync()
