import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_pressure_report():
    conn = sqlite3.connect(r"d:\works\AGrav\20_Проекты\sensors.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT DISTINCT p.id, p.model, p.full_name, c.name, p.description
        FROM product p
        JOIN category c ON p.category_id = c.id
        WHERE c.name LIKE '%давл%' OR p.full_name LIKE '%давл%' OR p.description LIKE '%давл%' OR p.model LIKE 'PS%'
    """)
    products = cursor.fetchall()
    
    with open(r"d:\works\AGrav\scratch\pressure_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Total products related to pressure: {len(products)}\n\n")
        for pid, model, fname, cat_name, desc in products:
            f.write(f"ID: {pid} | Model: {model} | Category: {cat_name}\n")
            f.write(f"Name: {fname}\n")
            f.write(f"Description: {desc}\n")
            
            cursor.execute("""
                SELECT param_name, param_value, nominal_value, numeric_value_min, numeric_value_max, unit
                FROM productspec
                WHERE product_id = ?
            """, (pid,))
            specs = cursor.fetchall()
            f.write("Specs:\n")
            for name, val, nom, n_min, n_max, unit in specs:
                f.write(f"  - {name}: {val} (min={n_min}, max={n_max}, unit={unit})\n")
            f.write("-" * 80 + "\n\n")
            
    conn.close()
    print("Report generated successfully.")

if __name__ == "__main__":
    generate_pressure_report()
