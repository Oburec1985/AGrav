import os
import sys
import glob
import json
from pathlib import Path

# Добавляем корневую директорию проекта в пути поиска, чтобы импортировать src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import BASE_DIR, RECORDS_DIR, COLLECTION_NAME
from src.database import MemoryDatabase

import math

def cosine_similarity(v1, v2):
    dot = sum(x * y for x, y in zip(v1, v2))
    norm1 = math.sqrt(sum(x * x for x in v1))
    norm2 = math.sqrt(sum(x * x for x in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def main():
    print("=== Запуск автоочистки и верификации MemoryDB ===")
    
    # 1. Инициализация базы данных
    db = MemoryDatabase()
    client = db.client
    
    workspace_root = BASE_DIR.parent.parent
    print(f"Корневая папка Workspace: {workspace_root}")
    
    # 2. Проверка битых ссылок на файлы
    print("\n1. Проверка ссылок на файлы...")
    json_files = glob.glob(str(RECORDS_DIR / "*.json"))
    deleted_count = 0
    
    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            source_file = data.get("source_file")
            if source_file:
                # Проверяем существование файла относительно корня workspace
                full_path = workspace_root / source_file
                if not full_path.exists():
                    print(f"[!] Файл источника не найден: {source_file}")
                    print(f"    Удаляем устаревший факт: {data.get('fact')[:60]}...")
                    # Удаляем JSON-файл
                    os.remove(file_path)
                    # Удаляем из Qdrant
                    db.delete_fact(data["id"])
                    deleted_count += 1
        except Exception as e:
            print(f"[Ошибка] Не удалось обработать файл {file_path}: {e}")
            
    print(f"Удалено неактуальных записей: {deleted_count}")

    # 3. Поиск семантических дубликатов в базе
    print("\n2. Поиск семантических дубликатов...")
    try:
        points, _ = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=10000,
            with_payload=True,
            with_vectors=True
        )
    except Exception as e:
        print(f"[Ошибка] Не удалось прочитать векторы из Qdrant: {e}")
        return

    # Находим дубликаты
    duplicates = []
    checked_pairs = set()
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            
            # Проверяем, что оба вектора доступны
            if p1.vector is None or p2.vector is None:
                continue
                
            sim = cosine_similarity(p1.vector, p2.vector)
            
            if sim > 0.95:  # Порог схожести 95% для косинусного сходства
                pair = tuple(sorted([p1.id, p2.id]))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    duplicates.append((p1, p2, sim))

    if duplicates:
        print(f"Найдены потенциальные дубликаты ({len(duplicates)}):")
        for p1, p2, sim in duplicates:
            print(f"\n[!] Сходство: {sim:.4f}")
            print(f"  Запись 1 ({p1.id}):")
            print(f"    ФАКТ: {p1.payload.get('fact')}")
            print(f"    ПРОЕКТ: {p1.payload.get('project_context')}")
            print(f"  Запись 2 ({p2.id}):")
            print(f"    ФАКТ: {p2.payload.get('fact')}")
            print(f"    ПРОЕКТ: {p2.payload.get('project_context')}")
            print("  -> Рекомендуется удалить один из файлов вручную или объединить их.")
    else:
        print("Дубликатов не обнаружено.")

    print("\n=== Очистка завершена успешно ===")

if __name__ == "__main__":
    main()
