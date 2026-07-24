import sqlite3

def query_db():
    conn = sqlite3.connect(r"d:\works\AGrav\20_Проекты\sensors.db")
    cursor = conn.cursor()
    
    # Посмотрим таблицы
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)
    
    # Посмотрим примеры продуктов
    cursor.execute("SELECT * FROM product LIMIT 5;")
    print("\nProducts:")
    for r in cursor.fetchall():
        print(r)
        
    # Посмотрим примеры характеристик
    cursor.execute("SELECT * FROM productspec LIMIT 5;")
    print("\nSpecs:")
    for r in cursor.fetchall():
        print(r)
        
    # Ищем датчики давления с temp_operating > 300
    # Категории датчиков:
    cursor.execute("SELECT * FROM category;")
    print("\nCategories:")
    for r in cursor.fetchall():
        print(r)
        
    conn.close()

if __name__ == "__main__":
    query_db()
