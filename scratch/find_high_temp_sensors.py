import sqlite3
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def find_high_temp_pressure_sensors():
    conn = sqlite3.connect(r"d:\works\AGrav\20_Проекты\sensors.db")
    cursor = conn.cursor()
    
    # Сначала найдем все продукты, связанные с динамическим давлением или вообще с давлением
    # Нам нужны именно датчики динамического давления.
    # Найдем все продукты, у которых в названии или описании есть слово "динамическ" и "давлени"
    # или просто "давлени", а потом отфильтруем по слову "динамическ" или "динамического давления"
    
    cursor.execute("""
        SELECT DISTINCT p.id, p.model, p.full_name, p.description
        FROM product p
        LEFT JOIN productspec ps ON p.id = ps.product_id
        WHERE (p.full_name LIKE '%давлен%' OR p.description LIKE '%давлен%' OR p.model LIKE 'PS%')
    """)
    products = cursor.fetchall()
    
    results = []
    
    for pid, model, fname, desc in products:
        # Для каждого продукта получим все характеристики
        cursor.execute("""
            SELECT param_name, param_value, nominal_value, numeric_value_min, numeric_value_max, unit
            FROM productspec
            WHERE product_id = ?
        """, (pid,))
        specs = cursor.fetchall()
        
        # Ищем температурные характеристики
        temp_spec = None
        is_dynamic = False
        
        # Проверяем, динамическое ли это давление
        # Обычно в названии или описании есть "динамическ" или "высокочастотн"
        text_to_check = (fname + " " + (desc or "")).lower()
        if "динамическ" in text_to_check or "dynamic" in text_to_check or model.startswith("PS"):
            is_dynamic = True
            
        for spec_name, spec_val, nom_val, n_min, n_max, unit in specs:
            # Нам нужны температурные характеристики
            name_lower = spec_name.lower()
            if any(k in name_lower for k in ["temp_operating", "температур", "температура", "temp"]):
                temp_spec = (spec_name, spec_val, n_min, n_max, unit)
                break
        
        if is_dynamic and temp_spec:
            spec_name, spec_val, n_min, n_max, unit = temp_spec
            # Проверим, больше ли максимальная температура 300 градусов
            # numeric_value_max может быть не заполнено, поэтому проверим и само значение по регулярке, и n_max
            max_temp = None
            if n_max is not None:
                max_temp = n_max
            else:
                # Попробуем распарсить из spec_val
                # например "от -55 до +125" или "до 350"
                nums = re.findall(r"[-+]?\d*\.?\d+", spec_val)
                if nums:
                    # обычно максимальная температура в конце диапазона
                    try:
                        max_temp = float(nums[-1])
                    except ValueError:
                        pass
            
            if max_temp is not None and max_temp >= 300:
                results.append({
                    "id": pid,
                    "model": model,
                    "name": fname,
                    "temp_val": spec_val,
                    "max_temp": max_temp,
                    "description": desc,
                    "specs": specs
                })
                
    # Сортируем по максимальной температуре (по убыванию)
    results.sort(key=lambda x: x["max_temp"], reverse=True)
    
    print(f"Found {len(results)} dynamic pressure sensors with temp >= 300°C:\n")
    for r in results:
        print(f"Model: {r['model']}")
        print(f"Name: {r['name']}")
        print(f"Temperature Range: {r['temp_val']} (Parsed max: {r['max_temp']}°C)")
        print(f"Description: {r['description']}")
        print("-" * 50)
        
    conn.close()

if __name__ == "__main__":
    find_high_temp_pressure_sensors()
