import os
import re
import logging
import yaml
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from sqlmodel import Session, select, create_engine, SQLModel, text
from app.models import Product, ProductSpec, Manufacturer, Category

# Детальное логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

# Поиск Vault
VAULT_ROOT = Path(r"C:\Users\User12345\Documents\Obsidian Vault")
VAULT_PATH = None
for p in VAULT_ROOT.rglob("GlobalTest_Sensors"):
    if p.is_dir():
        VAULT_PATH = p
        break

if not VAULT_PATH:
    logger.error("GlobalTest_Sensors directory NOT FOUND!")
    exit(1)

engine = create_engine(r"sqlite:///C:\Oburec\Antigravity\Projects\SQLSensorsDB\sensors.db")

def init_db():
    SQLModel.metadata.create_all(engine)

def clean_label(raw: str) -> str:
    return raw.replace("__", " ").replace("_", " ").replace("  ", " ").strip()

def get_canonical_name(raw_name: str) -> Optional[str]:
    raw_lower = clean_label(raw_name).lower()
    mapping = {
        "frequency_range": ["частот", "frequency"],
        "range_measure": ["диапазон", "range"],
        "sensitivity": ["чувствительность", "коэффициент", "sensitivity"],
        "accuracy_rel": ["относительная", "нелинейность", "linearity"],
        "accuracy_abs": ["абсолютная"],
        "accuracy_fs": ["приведенная", "шкала", "пш"],
        "temp_operating": ["температурный", "operating", "temp"],
        "humidity": ["влажност", "humidity"],
        "power_supply": ["питание", "power"],
        "input_current": ["входной ток", "ток потребления", "питания ток", "ток питания", "входной импеданс", "потребляемая мощность"],
        "weight_sensor": ["масса", "вес", "weight"],
        "dims_case": ["габариты", "размеры", "dimensions", "dims"],
        "connector": ["разъем", "разъём", "подключен", "соединител", "connector"],
        "mounting": ["крепление", "монтаж", "mounting"]
    }
    for canon, keys in mapping.items():
        if any(k in raw_lower for k in keys): return canon
    return None

"""
Модуль импорта данных (ETL: Obsidian -> SQLite)
-----------------------------------------------
Выполняет глубокий парсинг Markdown-файлов из хранилища Obsidian для заполнения базы данных SQL.

РЕШЕННЫЕ АРХИТЕКТУРНЫЕ ПРОБЛЕМЫ:
1. Проблема кодировок (Data Loss Bug):
   Файлы в Obsidian создавались в разных кодировках (Windows-1251 и UTF-8), причем иногда
   содержали единичные нечитаемые байты (например, 0x98). Строгий парсинг падал, из-за чего 
   в базу заливались пустые датчики (0 характеристик для 733 устройств).
   Решение: Внедрен "Каскад кодировок" (v14) -> сначала пытаемся прочитать как строгий UTF-8, 
   затем строгий CP1251. Если всё падает - включаем брутфорс CP1251 с флагом errors='replace'.

2. Утрата габаритов (x vs ×):
   Габариты (например, 12x22x22) в Obsidian часто записывались через математический знак
   умножения '×' (\xe2\x9c\x95 или \xd7), а не латинскую 'x'. Парсер считал последнюю цифру
   за "единицу измерения" (как в м/с2) и обрезал ее.
   Решение: В 'parse_val_with_unit' добавлена жесткая защита. Если в строке есть 'x' или '×',
   поиск юнитов регуляркой полностью отключается.

3. Range-Priority Aggregation (Перетирание допусков):
   При наличии 3-х файлов (напр. AP4000) для одного устройства, одиночная "частота резонанса 4,5" 
   перетирала полный рабочий диапазон "от 0.5 до 6000".
   Решение: Интеллектуальное слияние словарей. Характеристика, содержащая маркеры диапазона 
   ('-', 'до', 'от'), всегда имеет жесткий приоритет над одиночными числами.
"""

def parse_val_with_unit(val_str: str) -> Tuple[Optional[float], Optional[float], Optional[float], str]:
    if not val_str: return None, None, None, ""
    val_str = str(val_str).replace(',', '.').replace('±', '+/- ')
    
    # ЗАЩИТА ГАБАРИТОВ: Если есть латинская 'x' или математический знак '×', 
    # мы запрещаем парсеру искать "единицы измерения" в конце строки, чтобы не откусить цифру.
    unit = ""
    if 'x' not in val_str.lower() and '×' not in val_str.lower():
        unit_match = re.search(r'([a-zA-Z\u0410-\u044f\^/%]+)$', val_str.strip())
        unit = unit_match.group(1).lower() if unit_match else ""
    nums = re.findall(r"[-+]?\d*\.?\d+", val_str)
    if not nums: return None, None, None, unit
    try:
        if '+/-' in val_str or '±' in val_str:
            val = float(nums[0]); return val, -val, val, unit
        if any(x in val_str for x in ["до", "...", "–", "-"]):
            if len(nums) >= 2: return float(nums[1]), float(nums[0]), float(nums[1]), unit
        return float(nums[0]), None, None, unit
    except: return None, None, None, unit

def parse_md_file(file_path: Path) -> Dict[str, Any]:
    content = ""
    for enc in ['utf-8', 'cp1251']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
                # Если смогли прочитать без ошибок декодирования - это верная кодировка
                break
        except UnicodeDecodeError:
            continue
    
    if not content:
        # Третья линия обороны: игнорируем битые символы
        try:
            with open(file_path, 'r', encoding='cp1251', errors='replace') as f:
                content = f.read()
        except Exception:
            return None
        
    data = {"model": "", "full_name": "", "description": "", "specs": [], "image_url": None}
    
    # 1. Сначала ищем модель в YAML
    y = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if y:
        try:
            yd = yaml.safe_load(y.group(1))
            if yd:
                data["model"] = str(yd.get("model", "")).strip()
                data["full_name"] = str(yd.get("title", "")).strip()
        except: pass
    
    # 2. Если YAML пуст - берем из файла (самое надежное)
    if not data["model"]:
        m = re.sub(r'[^A-Z0-9-]', '', file_path.stem.upper())
        if len(m) >= 2: data["model"] = m

    # 3. ИЗВЛЕЧЕНИЕ ОПИСАНИЯ
    # Ищем блок между заголовком "## Описание" (или аналогами) и началом следующего раздела "##" или таблицы "|"
    desc_match = re.search(r'##\s*Описание\s*\n+(.*?)(?=\n##|\n\|)', content, re.DOTALL | re.IGNORECASE)
    if desc_match:
        # Убираем лишние подзаголовки (маркеры Markdown '#'), чтобы текст смотрелся чисто
        clean_desc = re.sub(r'#+\s+', '', desc_match.group(1)).strip()
        data["description"] = clean_desc

    # 3.5 ИЗВЛЕЧЕНИЕ ФОТОГРАФИИ
    img_match = re.search(r'!\[\[(.*?)\]\]|!\[.*?\]\((.*?)\)', content)
    if img_match:
        raw_name = img_match.group(1) if img_match.group(1) else img_match.group(2)
        if raw_name:
            clean_name = raw_name.split('|')[0].split('^')[0].split('/')[-1].strip()
            data["image_url"] = clean_name

    # 4. Описание и Таблицы
    h = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    if h and not data["full_name"]: data["full_name"] = h.group(1).strip()
    
    rows = re.findall(r'\|(.*?)\|(.*?)\|', content)
    for p, v in rows:
        p, v = p.strip(), v.strip()
        if p and v and p[0] != '-' and p.lower() != "параметр":
            data["specs"].append({"param": p, "value": v})
            
    return data

def import_all():
    init_db()
    with Session(engine) as session:
        session.execute(text("DELETE FROM productspec"))
        session.execute(text("DELETE FROM product"))
        session.commit()
        
        agg = {} # model -> { "data": d, "specs": { pk: val } }
        
        logger.info(f"Scanning vault: {VAULT_PATH}")
        
        image_index = {}
        for p in VAULT_PATH.rglob("*.*"):
            if p.suffix.lower() in [".jpg", ".png", ".jpeg", ".webp"]:
                image_index[p.name.lower()] = p
                
        local_attachments = Path(__file__).parent / "attachments"
        local_attachments.mkdir(parents=True, exist_ok=True)
        
        for root, _, files in os.walk(VAULT_PATH):
            for file in files:
                if not file.lower().endswith(".md"): continue
                
                model_name = re.sub(r'[^A-Z0-9-]', '', file.upper().replace(".MD", ""))
                if not model_name or len(model_name) < 2: continue
                
                d = parse_md_file(Path(os.path.join(root, file)))
                m = d["model"] if d and d.get("model") else model_name
                
                if m not in agg: agg[m] = {"data": d or {"description": "", "full_name": m, "specs": [], "image_url": None}, "specs": {}}
                if d and len(d.get("description", "")) > len(agg[m]["data"].get("description", "")):
                    agg[m]["data"]["description"] = d["description"]
                if d and d.get("image_url") and not agg[m]["data"].get("image_url"):
                    agg[m]["data"]["image_url"] = d["image_url"]
                
                if d:
                    for s in d["specs"]:
                        canon = get_canonical_name(s["param"])
                        pk = canon if canon else str(s["param"]).strip()
                        val = str(s["value"]).strip()
                        if not val or val == "---": continue
                        
                        # ПРИОРИТЕТ ДИАПАЗОНОВ (Range-Priority)
                        # Защита от перетирания: если в файле А указана резонансная частота "4.5", 
                        # а в файле Б "от 0.5 до 6000", мы отдаем предпочтение рабочему диапазону.
                        is_new_range = any(x in val.lower() for x in ["-", "до", ".", "от"])
                        old_val = agg[m]["specs"].get(pk, "")
                        is_old_range = any(x in old_val.lower() for x in ["-", "до", ".", "от"])
                        
                        if pk not in agg[m]["specs"] or (is_new_range and not is_old_range) or (len(val) > len(old_val) and not (is_old_range and not is_new_range)):
                            agg[m]["specs"][pk] = val

        logger.info(f"Total products to import: {len(agg)}")
        
        for m, entry in agg.items():
            d = entry["data"]
            prod = Product(model=m, full_name=d["full_name"] or m, description=d["description"], 
                           image_url=d.get("image_url"), manufacturer_id=1, category_id=1)
            session.add(prod); session.commit(); session.refresh(prod)
            
            if d.get("image_url"):
                img_name = d["image_url"].split('/')[-1]
                src_path = image_index.get(img_name.lower())
                if src_path:
                    try:
                        shutil.copy2(src_path, local_attachments / img_name)
                    except Exception as e:
                        logger.warning(f"Could not copy {img_name}: {e}")
            
            for pk, val_str in entry["specs"].items():
                nom, n_min, n_max, unit = parse_val_with_unit(val_str)
                if pk in ["dims_case", "connector", "mounting"] or 'x' in val_str.lower():
                    nom, n_min, n_max = None, None, None
                
                # Принудительные юниты
                if pk == "accuracy_rel" and not unit: unit = "%"
                if pk == "weight_sensor" and not unit: unit = "кг"
                if pk == "power_supply" and not unit: unit = "В"

                session.add(ProductSpec(
                    product_id=prod.id, 
                    group_name=next((g for g, ps in [
                        ("Метрология", ["range_measure", "sensitivity", "accuracy_rel", "accuracy_abs", "accuracy_fs", "frequency_range"]), 
                        ("Электрика", ["power_supply", "input_current", "output_signal", "output_range"]),
                        ("Условия", ["temp_operating", "humidity"]),
                        ("Конструктив", ["weight_sensor", "dims_case", "connector", "mounting"])
                    ] if pk in ps), "Прочее"),
                    param_name=pk, param_value=val_str, unit=unit,
                    nominal_value=nom, numeric_value_min=n_min, numeric_value_max=n_max
                ))
            session.commit()
    print(f"\nSUCCESS: Imported {len(agg)} products.")

if __name__ == "__main__":
    import_all()
