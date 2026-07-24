import sqlite3
import sys

# Настраиваем stdout на utf-8
sys.stdout.reconfigure(encoding='utf-8')

def check_categories_and_search():
    conn = sqlite3.connect(r"d:\works\AGrav\20_Проекты\sensors.db")
    cursor = conn.cursor()
    
    print("--- Categories ---")
    cursor.execute("SELECT id, name FROM category;")
    categories = cursor.fetchall()
    for cid, name in categories:
        print(f"ID: {cid}, Name: {name}")
        
    print("\n--- Searching for 'давления' or 'давление' in category or product specs ---")
    # Датчики давления. Поищем продукты, у которых в названии категории есть "давл" 
    # или у которых в specs есть слово "давление"
    cursor.execute("""
        SELECT p.id, p.model, p.full_name, c.name 
        FROM product p
        JOIN category c ON p.category_id = c.id
        WHERE c.name LIKE '%давл%' OR p.full_name LIKE '%давл%' OR p.description LIKE '%давл%';
    """)
    pressure_products = cursor.fetchall()
    print(f"Found {len(pressure_products)} products related to pressure")
    for pid, model, fname, cat_name in pressure_products[:20]:
        print(f"ID: {pid}, Model: {model}, Name: {fname}, Category: {cat_name}")
        
    conn.close()

if __name__ == "__main__":
    check_categories_and_search()
