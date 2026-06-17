import os
import sys

# Добавляем корневую директорию проекта в пути поиска, чтобы импортировать src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import MemoryDatabase

def main():
    print("=== Запуск локального теста MemoryDB ===")
    
    # 1. Инициализация базы
    print("1. Инициализация локального клиента Qdrant и FastEmbed...")
    db = MemoryDatabase()
    print("Успешно инициализировано.")
    
    # 2. Очистка прошлых тестовых записей (если есть)
    # Чтобы тесты были детерминированными, просто добавим новую запись
    print("\n2. Сохранение факта в базу...")
    fact_text = "В Lazarus (LCL) проектах (например, RecorderLnx) при сохранении файлов в cp1251 все русские строковые константы, присваиваемые свойствам компонентов LCL (Caption, Text, Items и т.д.) в коде, обязательно оборачивать в CP1251ToUTF8() из модуля LConvEncoding, иначе они отображаются знаками вопроса (????)."
    tags = ["lazarus", "encoding", "cp1251", "utf8"]
    project = "RecorderLnx"
    
    fact_id = db.save_fact(fact_text, tags, project)
    print(f"Факт успешно сохранен. ID: {fact_id}")
    
    # 3. Вывод списка фактов
    print("\n3. Просмотр списка фактов в базе:")
    facts = db.list_facts(limit=5)
    for f in facts:
        print(f"- [{f['project_context']}] (Tags: {f['tags']}): {f['fact'][:80]}...")
        
    # 4. Семантический поиск
    query = "как исправить знаки вопроса в русском тексте LCL на Lazarus?"
    print(f"\n4. Семантический поиск по запросу: '{query}'")
    results = db.search_facts(query, limit=3, project_context="RecorderLnx")
    
    print("Результаты поиска:")
    for i, res in enumerate(results, 1):
        print(f"{i}. [Score: {res['score']:.4f}] ID: {res['id']}")
        print(f"   ФАКТ: {res['fact']}")
        print(f"   ТЕГИ: {res['tags']}")
        print(f"   ПРОЕКТ: {res['project_context']}")
        
    print("\n=== Тест успешно завершен ===")

if __name__ == "__main__":
    main()
