import os
import sys
import builtins

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

# Добавляем корневую директорию проекта в пути поиска, чтобы импортировать src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import MemoryDatabase
from src.vault_indexer import VaultIndexer

def main():
    print("=== Тестирование индексатора базы знаний ===")
    
    db = MemoryDatabase()
    indexer = VaultIndexer(db)
    
    # 1. Пробный запуск (dry run)
    print("\n1. Выполнение пробного сканирования (dry run)...")
    res_dry = indexer.sync(dry_run=True)
    print(f"Результат dry run: {res_dry}")
    
    # 2. Выполнение реальной синхронизации
    print("\n2. Выполнение полной синхронизации (реальной)...")
    res_real = indexer.sync(dry_run=False)
    print(f"Результат реальной синхронизации: {res_real}")
    
    # 3. Проверка поиска
    # Поищем что-то, что наверняка есть в заметках AGrav (например, "Lazarus" или "DPI" или "RLM")
    query = "Что такое рекурсивный поиск RLM и как он устроен?"
    print(f"\n3. Тестирование семантического поиска по запросу: '{query}'")
    results = db.search_notes(query, limit=3)
    
    print("Результаты поиска:")
    for i, res in enumerate(results, 1):
        print(f"{i}. [Score: {res['score']:.4f}] Файл: {res['file_path']}")
        print(f"   Заголовок: {res['heading']}")
        print(f"   Контент:\n{res['content'][:150]}...")
        print("-" * 50)

if __name__ == "__main__":
    main()
