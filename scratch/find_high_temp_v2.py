import sqlite3
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def find_high_temp_pressure_sensors_v2():
    conn = sqlite3.connect(r"d:\works\AGrav\20_Проекты\sensors.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT DISTINCT p.id, p.model, p.full_name, p.description
        FROM product p
        WHERE p.full_name LIKE '%давлен%' OR p.description LIKE '%давлен%' OR p.model LIKE 'PS%'
    """)
    products = cursor.fetchall()
    
    results = []
    for pid, model, fname, desc in products:
        cursor.execute("""
            SELECT param_name, param_value, nominal_value, numeric_value_min, numeric_value_max, unit
            FROM productspec
            WHERE product_id = ?
        """, (pid,))
        specs = cursor.fetchall()
        
        # Ищем любые характеристики, где упоминается температура или градусы Цельсия
        temp_specs = []
        for name, val, nom, n_min, n_max, unit in specs:
            val_lower = val.lower()
            name_lower = name.lower()
            
            # Признаки температурной характеристики:
            # 1. В названии параметра есть "темп" или "temp"
            # 2. В значении параметра есть "°С" или "°c" или " градусов"
            # 3. В юните есть "с" или "c" (но надо аккуратно, т.к. "с" может быть секундами, хотя обычно для температуры)
            is_temp = False
            if any(k in name_lower for k in ["temp", "темп"]):
                is_temp = True
            elif any(k in val_lower for k in ["°с", "°c", " c", " с"]):
                # исключаем ложные срабатывания, например, "м/с"
                if "м/с" not in val_lower and "пф" not in val_lower:
                    is_temp = True
                    
            if is_temp:
                temp_specs.append((name, val, n_min, n_max, unit))
                
        if temp_specs:
            # Для найденных температурных характеристик проверим максимальное значение
            for name, val, n_min, n_max, unit in temp_specs:
                # Извлечем все числа
                nums = re.findall(r"[-+]?\d*\.?\d+", val.replace(',', '.'))
                if nums:
                    try:
                        # Ищем максимальное число
                        # Исключим отрицательные числа и выберем максимум
                        parsed_nums = [float(n) for n in nums]
                        max_val = max(parsed_nums)
                        if max_val >= 300:
                            results.append({
                                "model": model,
                                "name": fname,
                                "desc": desc,
                                "temp_param": name,
                                "temp_val": val,
                                "max_temp": max_val
                            })
                            break # Прекращаем проверку других спек для этого продукта, если нашли подходящую
                    except ValueError:
                        pass
                        
    # Сортируем по модели
    results.sort(key=lambda x: x["model"])
    
    print(f"Found {len(results)} pressure sensors with temp >= 300°C:")
    for r in results:
        print(f"\nМодель: {r['model']}")
        print(f"Название: {r['name']}")
        print(f"Характеристика температуры: {r['temp_param']}: {r['temp_val']} (Макс: {r['max_temp']}°C)")
        print(f"Описание: {r['desc']}")
        print("-" * 60)
        
    conn.close()

if __name__ == "__main__":
    find_high_temp_pressure_sensors_v2()
