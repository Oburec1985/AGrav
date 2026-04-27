import os
import glob
import json
import csv
import sys
import subprocess
import re
import urllib.request
import ctypes
import traceback
import logging
import datetime
import time
import difflib
from concurrent.futures import ThreadPoolExecutor, as_completed

def ensure_dependencies():
    """Checks and installs missing python packages automatically."""
    required = ["pytesseract", "opencv-python", "pillow", "numpy", "requests"]
    import_map = {"opencv-python": "cv2", "pillow": "PIL"}
    
    for pkg in required:
        mod = import_map.get(pkg, pkg)
        try:
            __import__(mod)
        except ImportError:
            print(f"Installing missing dependency: {pkg}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            except Exception as e:
                print(f"Error installing {pkg}: {e}")

# Запускаем проверку до всех остальных импортов
ensure_dependencies()

import cv2
import numpy as np
import pytesseract

# Для работы требуется: py -m pip install pytesseract Pillow opencv-python numpy
# И установленный Tesseract OCR в системе.

def log(message, level="INFO"):
    """Кастомная функция логирования."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] [{level}] {message}"
    try:
        # Для консоли пробуем utf-8, если не выйдет - системную
        print(msg.encode('utf-8', errors='replace').decode('utf-8'))
    except:
        print(msg)
        
    try:
        # В файл пишем в cp1251 для совместимости с инструментами пользователя
        with open("ocr.log", "a", encoding="cp1251", errors="replace") as f:
            f.write(msg + "\n")
    except Exception as e:
        print(f"Ошибка записи в лог: {e}")

def reset_log():
    """Очищает лог перед новым запуском скрипта."""
    try:
        with open("ocr.log", "w", encoding="cp1251", errors="replace") as f:
            f.write("")
    except Exception as e:
        print(f"Ошибка очистки лога: {e}")


def download_file(url, filename):
    """Скачивает файл с индикацией прогресса."""
    log(f"Начинаю скачивание {os.path.basename(filename)}...")
    try:
        urllib.request.urlretrieve(url, filename)
        log(f"Скачивание завершено: {filename}")
        return True
    except Exception as e:
        log(f"Ошибка при скачивании {url}: {e}", "ERROR")
        return False

def get_short_path_name(long_name):
    """Преобразует длинный путь в короткий (8.3) для совместимости с Tesseract на Windows."""
    if not long_name:
        return ""
    try:
        output_buf_size = 0
        while True:
            output_buf = ctypes.create_unicode_buffer(output_buf_size)
            needed = ctypes.windll.kernel32.GetShortPathNameW(long_name, output_buf, output_buf_size)
            if output_buf_size >= needed:
                return output_buf.value
            output_buf_size = needed
    except Exception as e:
        log(f"Предупреждение: не удалось получить короткий путь для {long_name}: {e}", "WARNING")
        return long_name

def ensure_rus_language():
    """Проверяет наличие русского языка и скачивает его при необходимости."""
    import pytesseract
    
    # Пытаемся найти, где лежит tesseract
    tess_cmd = pytesseract.pytesseract.tesseract_cmd
    if not tess_cmd or tess_cmd == 'tesseract':
        # Попробуем найти в PATH или стандартных местах
        common_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        ]
        for path in common_paths:
            if os.path.exists(path):
                tess_cmd = path
                pytesseract.pytesseract.tesseract_cmd = path
                break

    # Определяем системную папку tessdata
    sys_tessdata = ""
    if tess_cmd and os.path.exists(tess_cmd):
        sys_tessdata = os.path.join(os.path.dirname(tess_cmd), "tessdata")
    
    # Проверяем наличие rus.traineddata в системе
    if sys_tessdata and os.path.exists(os.path.join(sys_tessdata, "rus.traineddata")):
        return "" # Все ок, есть в системе

    # Если в системе нет, создаем локальную папку
    local_tessdata_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tessdata")
    if not os.path.exists(local_tessdata_dir):
        os.makedirs(local_tessdata_dir)
    
    rus_path = os.path.join(local_tessdata_dir, "rus.traineddata")
    log(f"Проверка языкового пакета: {rus_path}")
    if not os.path.exists(rus_path):
        url = "https://github.com/tesseract-ocr/tessdata/raw/main/rus.traineddata"
        if not download_file(url, rus_path):
            log("КРИТИЧЕСКАЯ ОШИБКА: Не удалось скачать языковой пакет 'rus'.", "ERROR")
            log(f"Пожалуйста, скачайте его вручную и положите в: {rus_path}", "ERROR")
            return ""
    
    # Также скачиваем eng.traineddata для лучшего распознавания знаков и букв
    eng_url = "https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata"
    eng_path = os.path.join(local_tessdata_dir, "eng.traineddata")
    if not os.path.exists(eng_path):
        log(f"Скачивание eng.traineddata в {eng_path}...")
        try:
            import urllib.request
            urllib.request.urlretrieve(eng_url, eng_path)
            log("eng.traineddata скачан.")
        except Exception as e:
            log(f"Не удалось скачать eng.traineddata: {e}", "WARNING")

    # Возвращаем короткий путь для гарантированной работы Tesseract
    return get_short_path_name(local_tessdata_dir)

def ensure_dependencies():
    """Проверяет наличие необходимых библиотек и устанавливает их при отсутствии."""
    dependencies = {
        "pytesseract": "pytesseract",
        "PIL": "Pillow",
        "cv2": "opencv-python",
        "numpy": "numpy"
    }
    for module, package in dependencies.items():
        try:
            __import__(module)
        except ImportError:
            log(f"Библиотека {module} не найдена. Установка {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                log(f"Библиотека {package} успешно установлена.")
            except Exception as e:
                log(f"Ошибка при установке {package}: {e}", "ERROR")
    
    # Проверка бинарного движка Tesseract
    import pytesseract
    try:
        pytesseract.get_tesseract_version()
    except Exception:
        # Пытаемся найти в стандартных путях, если его нет в PATH
        common_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Tesseract-OCR", "tesseract.exe")
        ]
        found = False
        for path in common_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                try:
                    pytesseract.get_tesseract_version()
                    found = True
                    break
                except Exception:
                    continue
        
        if not found:
            log("Tesseract не найден в системе.", "ERROR")

def log_runtime_info():
    """Пишет в лог интерпретатор и версии ключевых OCR-библиотек."""
    log(f"Python executable: {sys.executable}")
    log(f"Python version: {sys.version.split()[0]}")
    log(f"Working directory: {os.getcwd()}")

    modules = [
        ("cv2", "OpenCV"),
        ("numpy", "NumPy"),
        ("PIL", "Pillow"),
        ("pytesseract", "pytesseract"),
    ]
    for module_name, display_name in modules:
        try:
            module = __import__(module_name)
            version = getattr(module, "__version__", "unknown")
            log(f"{display_name} version: {version}")
        except Exception as e:
            log(f"{display_name} version: недоступно ({e})", "WARNING")

    try:
        import pytesseract
        log(f"Tesseract version: {pytesseract.get_tesseract_version()}")
        log(f"Tesseract command: {pytesseract.pytesseract.tesseract_cmd}")
    except Exception as e:
        log(f"Tesseract version: недоступно ({e})", "WARNING")

def extract_data_from_text(text, filename=""):
    """Извлекает ФИО и суммы из текста с помощью регулярных выражений."""
    results = []
    # Ищем паттерн: Фамилия И.О. (или просто Фамилия) и число
    pattern = r"([А-ЯЁ][а-яё\-]+(?:\s+[А-ЯЁ]\.(?:\s*[А-ЯЁ]\.)?)?)\s+.*?(\d+[\.,\s]?\d+[\.,]\d+|\d+[\.,]\d+|\d+)"
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        
        match = re.search(pattern, line)
        if match:
            name = match.group(1).strip()
            value_str = match.group(2).replace(' ', '').replace(',', '.')
            try:
                val = float(value_str)
                results.append((name, val))
                log(f"[{filename}] Найдено: {name} -> {val}")
            except ValueError:
                log(f"[{filename}] Ошибка парсинга суммы в строке: {line}", "WARNING")
        else:
            if any(c.isdigit() for c in line) and any(c >= 'А' and c <= 'я' for c in line):
                 log(f"[{filename}] Не удалось распарсить строку с данными: {line}", "DEBUG")
    return results

def load_employees(filename):
    """Загружает список сотрудников из файла."""
    if not os.path.exists(filename):
        return []
    # Пробуем разные кодировки
    for enc in ["utf-8", "cp1251"]:
        try:
            with open(filename, "r", encoding=enc) as f:
                return [line.strip() for line in f if line.strip()]
        except:
            continue
    return []

def normalize_employee_name(name):
    """Нормализует ФИО для сравнения OCR с employees.txt."""
    text = (name or "").upper().replace("Ё", "Е")
    months = [
        "ЯНВАРЬ", "ЯНВАР", "ФЕВРАЛЬ", "МАРТ", "АПРЕЛЬ", "МАЙ", "ИЮНЬ",
        "ИЮЛЬ", "АВГУСТ", "СЕНТЯБРЬ", "ОКТЯБРЬ", "НОЯБРЬ", "ДЕКАБРЬ",
    ]
    for month in months:
        text = text.replace(month, " ")
    text = re.sub(r'\b20\d{2}\b', ' ', text)
    text = re.sub(r'[^А-ЯA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_ocr_name(text):
    """Очищает OCR заголовка, сохраняя русские буквы, точки и дефисы и убирая месяц."""
    text = (text or "").replace("\n", " ")
    text = re.sub(r'[^А-Яа-яЁё\s\.\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    months = [
        "ЯНВАРЬ", "ЯНВАР", "ФЕВРАЛЬ", "ФЕВРАЛ", "МАРТ", "АПРЕЛЬ", "МАЙ", "ИЮНЬ",
        "ИЮЛЬ", "АВГУСТ", "СЕНТЯБРЬ", "ОКТЯБРЬ", "НОЯБРЬ", "ДЕКАБРЬ",
    ]
    for month in months:
        text = re.sub(rf'\b{month}\w*\b', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip(" .-")
    return text

def surname_of(name):
    norm = normalize_employee_name(name)
    return norm.split()[0] if norm else ""

def initials_tail(name):
    """Возвращает часть имени после фамилии для различения однофамильцев."""
    text = clean_ocr_name(name).upper().replace("Ё", "Е")
    parts = text.split(None, 1)
    if len(parts) < 2:
        return ""
    return re.sub(r'[^А-ЯA-Z\-]', '', parts[1])

def match_employee_name(ocr_name, dictionary):
    """Возвращает эталонное имя из словаря и коэффициент похожести."""
    if not dictionary:
        return ocr_name, 0.0, []

    norm_ocr = normalize_employee_name(ocr_name)
    ocr_surname = surname_of(ocr_name)
    ocr_tail = initials_tail(ocr_name)
    scores = []
    for employee in dictionary:
        norm_employee = normalize_employee_name(employee)
        emp_surname = surname_of(employee)
        emp_tail = initials_tail(employee)

        full_score = difflib.SequenceMatcher(None, norm_ocr, norm_employee).ratio()
        surname_score = difflib.SequenceMatcher(None, ocr_surname, emp_surname).ratio() if ocr_surname else 0.0
        tail_score = difflib.SequenceMatcher(None, ocr_tail, emp_tail).ratio() if ocr_tail and emp_tail else 0.0

        score = max(full_score, 0.72 * surname_score + 0.28 * full_score)
        if ocr_surname and emp_surname and ocr_surname == emp_surname and emp_tail:
            score = 0.55 * surname_score + 0.20 * full_score + 0.25 * tail_score

        scores.append((score, employee, norm_employee))

    scores.sort(reverse=True, key=lambda item: item[0])
    best_score, best_employee, _ = scores[0]
    if best_score < 0.2: # Если совпадение слишком слабое, считаем что не нашли
        return "", 0.0, scores[:3]
    return best_employee, best_score, scores[:3]

def choose_employee_name(ocr_name, employee_dict, block_num):
    """Выбирает ближайшее ФИО из словаря по OCR заголовка."""
    if not employee_dict:
        return ocr_name

    matched_name, match_score, top_matches = match_employee_name(ocr_name, employee_dict)
    top_text = ", ".join(f"{emp}:{score:.2f}" for score, emp, _ in top_matches)

    if match_score >= 0.45:
        log(f"Блок {block_num}: OCR имени '{ocr_name}' -> '{matched_name}' ({match_score:.3f}). Топ: {top_text}")
        return matched_name

    log(
        f"Блок {block_num}: слабое сопоставление имени OCR '{ocr_name}' ({match_score:.3f}), "
        f"используем лучший словарный вариант '{matched_name}'. Топ: {top_text}",
        "WARNING",
    )
    return matched_name

def ocr_cell(img_cv, lang='rus', config='--psm 7'):
    """Распознает текст в отдельной ячейке."""
    import pytesseract
    import cv2
    from PIL import Image
    
    # Убираем линии сетки по краям ячейки: они особенно мешают OCR в правых блоках.
    h, w = img_cv.shape[:2]
    if h > 8 and w > 8:
        pad_y = max(1, min(3, h // 10))
        pad_x = max(1, min(3, w // 20))

    # Масштабируем ячейку для лучшего OCR
    h, w = img_cv.shape[:2]
    if h < 40:
        scale = 6.0 # Возвращаем 6x для очень мелкого текста
        img_cv = cv2.resize(img_cv, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_LANCZOS4)
    
    # Предобработка: ч/б -> повышение контраста -> порог
    if len(img_cv.shape) == 3:
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Убираем шум
    img_cv = cv2.medianBlur(img_cv, 3)
    
    # Адаптивный порог для выделения текста на разном фоне
    thresh = cv2.adaptiveThreshold(img_cv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Инвертируем, если текст светлый на темном (обычно наоборот, но на всякий случай)
    # Но Tesseract лучше работает с черным текстом на белом фоне.
    # Проверим среднее значение по краям
    edge_mean = (thresh[0,:].mean() + thresh[-1,:].mean() + thresh[:,0].mean() + thresh[:,-1].mean()) / 4
    if edge_mean < 127:
        thresh = cv2.bitwise_not(thresh)

    pil_img = Image.fromarray(thresh)
    try:
        return pytesseract.image_to_string(pil_img, lang=lang, config=config).strip()
    except Exception as e:
        log(f"Ошибка OCR ячейки: {e}", "DEBUG")
        return ""

def ocr_name_cell(img_cv, config=""):
    """Распознает маленькую ячейку ФИО несколькими режимами под русские буквы."""
    import pytesseract
    import cv2
    from PIL import Image

    if len(img_cv.shape) == 3:
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        gray = img_cv

    # Для имен на сером фоне адаптивный порог и Оцу
    h, w = gray.shape[:2]
    scale = 8
    gray = cv2.resize(gray, (w * scale, h * scale), interpolation=cv2.INTER_LANCZOS4)
    
    variants = []
    # 1. Адаптивный порог с большим окном
    variants.append(("adaptive", cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 15)))
    # 2. Оцу
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants.append(("otsu", otsu))
    # 3. Оригинальный серый
    variants.append(("gray", gray))

    # Убираем whitelist для теста, если он мешает
    base_config = f"{config}".strip()
    psm_configs = [6, 7]

    candidates = []
    seen = set()

    def run_ocr(variant_info):
        v_name, prep, psm = variant_info
        try:
            ocr_config = f"--psm {psm} {base_config}".strip()
            text = pytesseract.image_to_string(Image.fromarray(prep).convert('L'), lang='rus+eng', config=ocr_config).strip()
            cleaned = clean_ocr_name(text)
            if cleaned:
                return (cleaned, text, v_name, ocr_config)
        except Exception:
            pass
        return None

    tasks = []
    for variant_name, prepared in variants:
        padded = cv2.copyMakeBorder(prepared, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=255)
        for psm in psm_configs:
            tasks.append((variant_name, padded, psm))

    # Используем ThreadPoolExecutor для параллельного запуска Tesseract
    with ThreadPoolExecutor(max_workers=min(len(tasks), 10)) as executor:
        future_to_task = {executor.submit(run_ocr, task): task for task in tasks}
        for future in as_completed(future_to_task):
            res = future.result()
            if res:
                cleaned, text, variant_name, ocr_config = res
                key = cleaned.upper()
                if key not in seen:
                    seen.add(key)
                    candidates.append(res)

    return candidates

def parse_amount(value_str):
    """Достает число из OCR-текста денежной ячейки."""
    if not value_str:
        return 0
    value_str = value_str.replace(' ', '').replace(',', '.')
    match = re.search(r'(-?\d+[\.,]\d+|-?\d+)', value_str)
    if not match:
        return 0
    try:
        val_str = match.group(1).replace(',', '.')
        val = float(val_str)
        # Специфический фикс для этих таблиц: если в конце "1", и число вылетает за 500к,
        # это почти наверняка полоса сетки, которую Tesseract принял за единицу.
        # Также проверяем на аномально длинные числа.
        if val > 550000 and val_str.endswith('1'):
            return val // 10
        return val
    except ValueError:
        return 0

def amount_is_plausible(value):
    """Отсекает явный OCR-мусор для итоговой выплаты."""
    return 50000 <= value <= 500000

def ocr_amount_cell(img_cv, config=""):
    """Распознает маленькую числовую ячейку несколькими режимами OCR."""
    import pytesseract
    import cv2
    from PIL import Image

    h, w = img_cv.shape[:2]
    # Обрезаем только 1 пиксель, чтобы убрать сетку, не повредив цифры
    if h > 10 and w > 10:
        img_cv = img_cv[1:h-1, 1:w-1]

    if len(img_cv.shape) == 3:
        gray_orig = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        gray_orig = img_cv

    variants = []
    # Вариант 1: 5x + Adaptive (Вес 1.0)
    scale5 = 5
    gray5 = cv2.resize(gray_orig, (gray_orig.shape[1] * scale5, gray_orig.shape[0] * scale5), interpolation=cv2.INTER_LANCZOS4)
    gray5 = cv2.copyMakeBorder(gray5, 30, 30, 30, 30, cv2.BORDER_CONSTANT, value=255)
    variants.append(("scale5_adapt", cv2.adaptiveThreshold(gray5, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11), 1.0, 1))

    # Вариант 2: 8x + Оцу (Вес 1.0)
    scale8 = 8
    gray8 = cv2.resize(gray_orig, (gray_orig.shape[1] * scale8, gray_orig.shape[0] * scale8), interpolation=cv2.INTER_LANCZOS4)
    gray8 = cv2.copyMakeBorder(gray8, 30, 30, 30, 30, cv2.BORDER_CONSTANT, value=255)
    _, otsu8 = cv2.threshold(gray8, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants.append(("scale8_otsu", otsu8, 1.0, 1))
    
    # Вариант 3: Legacy движок (OEM 0) - часто лучше на цифрах (Вес 0.8)
    variants.append(("legacy", otsu8, 0.8, 0))
    
    # Вариант 4: Утончение (Erosion) - (Вес 0.5)
    kernel = np.ones((2, 2), np.uint8)
    eroded = cv2.erode(otsu8, kernel, iterations=1)
    variants.append(("eroded", eroded, 0.5, 1))

    # Вариант 5: Повышенный контраст (Вес 0.7)
    contrast = cv2.convertScaleAbs(gray8, alpha=1.5, beta=-30)
    _, otsu_c = cv2.threshold(contrast, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants.append(("contrast", otsu_c, 0.7, 1))

    # Вариант 6: CLAHE (Локальный контраст) (Вес 0.6)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl1 = clahe.apply(gray8)
    variants.append(("clahe", cv2.adaptiveThreshold(cl1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 15), 0.6, 1))

    # Вариант 7: Гамма-коррекция (затягивание серого в черный) (Вес 0.8)
    gamma = 0.5
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    gamma_img = cv2.LUT(gray8, table)
    _, otsu_g = cv2.threshold(gamma_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants.append(("gamma", otsu_g, 0.8, 1))

    # Вариант 8: Утолщение черного (захват серых пикселей) (Вес 0.7)
    _, hard_thresh = cv2.threshold(gray8, 190, 255, cv2.THRESH_BINARY)
    kernel_thick = np.ones((2, 2), np.uint8)
    thick = cv2.erode(hard_thresh, kernel_thick, iterations=1) 
    variants.append(("thick", thick, 0.7, 1))

    # Используем встроенный конфиг 'digits'
    base_config = f"digits -c tessedit_char_whitelist=0123456789,. {config}".strip()
    psm_configs = [6, 7] # Оставляем самые надежные

    candidates = []
    
    def run_ocr(variant_info):
        v_name, prep, psm, weight, oem = variant_info
        try:
            ocr_config = f"--oem {oem} --psm {psm} {base_config}".strip()
            text = pytesseract.image_to_string(Image.fromarray(prep).convert('L'), lang='rus+eng', config=ocr_config).strip()
            value = parse_amount(text)
            if value:
                return (value, text, v_name, ocr_config, weight)
        except Exception:
            pass
        return None

    tasks = []
    for variant_name, prepared, weight, oem in variants:
        for psm in psm_configs:
            tasks.append((variant_name, prepared, psm, weight, oem))

    with ThreadPoolExecutor(max_workers=min(len(tasks), 10)) as executor:
        future_to_task = {executor.submit(run_ocr, task): task for task in tasks}
        for future in as_completed(future_to_task):
            res = future.result()
            if res:
                candidates.append(res)

    if not candidates:
        return "", 0, []

    plausible = [item for item in candidates if amount_is_plausible(item[0])]
    pool = plausible if plausible else candidates

    # Взвешенное голосование
    buckets = {}
    for value, text, variant_name, ocr_config, weight in pool:
        key = round(value)
        buckets.setdefault(key, 0)
        buckets[key] += weight
    
    best_key = max(buckets, key=lambda key: buckets[key])
    
    # Находим любой из результатов, давших этот ключ
    for value, text, variant_name, ocr_config, weight in pool:
        if round(value) == best_key:
            return text, value, candidates
    
    return "", 0, candidates

def compact_text(text, limit=80):
    """Готовит OCR-текст для однострочного диагностического лога."""
    text = (text or "").replace("\r", "\\r").replace("\n", "\\n").strip()
    if len(text) > limit:
        return text[:limit] + "..."
    return text

def build_salary_blocks(x_coords):
    """Группирует вертикальные линии в независимые зарплатные блоки."""
    blocks = []

    # В этих JPG каждый блок - отдельная мини-таблица из трех вертикальных линий:
    # левая граница, разделитель "начисление/значение", правая граница.
    if len(x_coords) >= 3 and len(x_coords) % 3 == 0:
        for i in range(0, len(x_coords) - 2, 3):
            x1, x2, x3 = x_coords[i], x_coords[i+1], x_coords[i+2]
            label_w = x2 - x1
            value_w = x3 - x2
            if label_w >= 40 and value_w >= 35:
                blocks.append((i, x1, x2, x3))

        if len(blocks) == len(x_coords) // 3:
            return blocks

    # Запасной режим для таблиц без зазоров между блоками.
    for i in range(0, len(x_coords) - 2, 2):
        x1, x2, x3 = x_coords[i], x_coords[i+1], x_coords[i+2]
        if x2 - x1 >= 40 and x3 - x2 >= 35:
            blocks.append((i, x1, x2, x3))
    return blocks

def is_payout_row_label(text):
    """Целевая строка итоговой выплаты."""
    text = (text or "").upper().strip()
    text = re.sub(r'\s+', ' ', text)
    if not text:
        return False
    if "ИТОГО К ВЫПЛАТЕ" in text:
        return True
    if "К ВЫПЛАТЕ" in text and "ИТОГО" in text:
        return True
    ratio = difflib.SequenceMatcher(None, text, "ИТОГО К ВЫПЛАТЕ").ratio()
    return ratio > 0.68

def parse_image(image_path, tessdata_dir="", employee_dict=None):
    try:
        import pytesseract
        from PIL import Image
        import cv2
        
        image_name = os.path.basename(image_path)

        # Загрузка
        with open(image_path, "rb") as f:
            chunk = np.frombuffer(f.read(), dtype=np.uint8)
            img = cv2.imdecode(chunk, cv2.IMREAD_COLOR)
        if img is None: return []
        log(f"Файл {image_name}: размер {img.shape[1]}x{img.shape[0]}", "DEBUG")
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        
        # Конфигурация Tesseract
        config = ""
        if tessdata_dir:
            tessdata_dir = os.path.normpath(tessdata_dir).rstrip('\\/')
            if "~" in tessdata_dir or " " not in tessdata_dir:
                config = f'--tessdata-dir {tessdata_dir}'
            else:
                config = f'--tessdata-dir "{tessdata_dir}"'

        # Линии
        h_size = max(1, img.shape[1] // 30)
        v_size = max(1, img.shape[0] // 30)
        h_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (h_size, 1))
        v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, v_size))
        
        h_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, h_kernel, iterations=2)
        v_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, v_kernel, iterations=2)
        
        # Координаты сетки
        def get_coords(line_img, is_vertical=True):
            proj = np.sum(line_img, axis=0 if is_vertical else 1)
            coords = []
            thresh_val = np.max(proj) * 0.3
            in_line = False
            start = 0
            for i, val in enumerate(proj):
                if val > thresh_val and not in_line:
                    start = i; in_line = True
                elif val < thresh_val and in_line:
                    coords.append((start + i) // 2); in_line = False
            if in_line:
                coords.append((start + len(proj) - 1) // 2)
            return coords

        def merge_close_coords(coords, min_gap=4):
            if not coords:
                return []
            merged = []
            group = [coords[0]]
            for coord in coords[1:]:
                if coord - group[-1] <= min_gap:
                    group.append(coord)
                else:
                    merged.append(int(round(sum(group) / len(group))))
                    group = [coord]
            merged.append(int(round(sum(group) / len(group))))
            return merged

        x_coords = merge_close_coords(sorted(get_coords(v_lines, True)))
        y_coords = merge_close_coords(sorted(get_coords(h_lines, False)))
        
        log(f"Найдено линий: X={len(x_coords)}, Y={len(y_coords)}")
        
        if len(x_coords) < 2 or len(y_coords) < 2:
            log("Сетка не найдена, переход к обычному OCR", "WARNING")
            # Fallback to simple OCR
            text = pytesseract.image_to_string(Image.fromarray(gray), lang='rus', config='--psm 6')
            return extract_data_from_text(text, os.path.basename(image_path))

        salary_blocks = build_salary_blocks(x_coords)
        if not salary_blocks:
            log("Не удалось сгруппировать вертикальные линии в зарплатные блоки.", "ERROR")
            return []

        # Быстрый проход: строки в зарплатных блоках совпадают, поэтому ищем
        # целевую строку только в нижней части первых блоков, а не во всей таблице.
        cell_config = f"--psm 7 {config}".strip()
        common_total_row = -1
        visual_expected_row = 20 if len(y_coords) > 21 else (len(y_coords) - 6 if len(y_coords) >= 7 else -1)

        log(f"Найдено зарплатных блоков: {len(salary_blocks)}", "INFO")

        if visual_expected_row != -1:
            common_total_row = visual_expected_row
            log(f"Определена ожидаемая строка ИТОГО К ВЫПЛАТЕ по умолчанию: индекс {common_total_row}")
        
        # Кэш индекса строки, если она будет найдена динамически в первом блоке
        cached_total_row = -1

        results = []

        # Формируем общий конфиг для ячеек
        config_with_tessdata = f'--tessdata-dir "{tessdata_dir}"' if " " in tessdata_dir else f'--tessdata-dir {tessdata_dir}'
        cell_config = f"--psm 7 {config_with_tessdata}".strip()
        
        # Сначала обрабатываем первый блок, чтобы найти строку ИТОГО, если она не совпадает с дефолтом
        # Для простоты объединим в один цикл, но будем обновлять cached_total_row.
        
        for block_num, (col_idx, x1, x2, x3) in enumerate(salary_blocks, start=1):
            # 1. Извлекаем ФИО из левой ячейки заголовка. Правая ячейка содержит месяц,
            # поэтому распознавание x1:x3 часто портит ФИО.
            name_candidates = []
            name_left_img = gray[y_coords[0]:y_coords[1], x1:x2]
            name_candidates.extend(ocr_name_cell(name_left_img, config=config_with_tessdata))

            # Если левая ячейка не дала кандидатов, пробуем заголовок целиком.
            if not name_candidates:
                name_full_img = gray[y_coords[0]:y_coords[1], x1:x3]
                name_candidates.extend(ocr_name_cell(name_full_img, config=config_with_tessdata))

            if name_candidates and employee_dict:
                scored_candidates = []
                for cleaned_name, raw_text, variant_name, ocr_config in name_candidates:
                    matched_name, match_score, _ = match_employee_name(cleaned_name, employee_dict)
                    scored_candidates.append((match_score, cleaned_name, matched_name, variant_name, raw_text))
                scored_candidates.sort(reverse=True, key=lambda item: item[0])
                best_score, name, best_match, best_variant, raw_name = scored_candidates[0]
                log(f"Блок {block_num}: лучший OCR ФИО '{name}' ({best_variant}, score={best_score:.3f}) -> '{best_match}'")
            elif name_candidates:
                name = name_candidates[0][0]
            else:
                name = f"Unknown_{x1}"

            log(f"Обработка колонки человека: {name}")

            # Коррекция по словарю по ближайшему совпадению OCR
            if employee_dict:
                name = choose_employee_name(name, employee_dict, block_num)
            
            if not name or len(name) < 3:
                continue # Пропускаем пустые колонки или колонки только с месяцем
            
            log(f"Имя после очистки и коррекции: {name}")
            person_sum = 0
            
            # Формируем список строк для проверки
            check_rows = []
            
            # 1. Приоритет: кэшированная строка или дефолтная
            if cached_total_row != -1:
                check_rows.append(cached_total_row)
            elif common_total_row != -1:
                check_rows.append(common_total_row)
            
            # 2. Если ничего не подошло, сканируем диапазон
            candidate_rows = list(range(max(1, len(y_coords) - 9), len(y_coords) - 1))
            for r in candidate_rows:
                if r not in check_rows:
                    check_rows.append(r)
            
            for row_idx in check_rows:
                y1, y2 = y_coords[row_idx], y_coords[row_idx+1]
                
                cat_img = gray[y1:y2, x1:x2]
                val_img = gray[y1:y2, x2:x3]
                
                category = ""
                # Если это не общая строка, проверяем ключевое слово
                if row_idx != common_total_row:
                    category = ocr_cell(cat_img, config=cell_config)
                    if not is_payout_row_label(category):
                        # Попробуем во всем блоке
                        full_cell_img = gray[y1:y2, x1:x3]
                        full_text = ocr_cell(full_cell_img, config=cell_config)
                        if is_payout_row_label(full_text):
                            category = full_text
                        else:
                            continue # Не та строка
                else:
                    category = "ИТОГО К ВЫПЛАТЕ (геометрия)"

                # Если дошли сюда, значит это либо общая строка ИТОГО, либо найден ключ в текущей
                value_str, val, _ = ocr_amount_cell(val_img, config=config_with_tessdata)
                
                # Попытка вытащить число из категории, если в значении пусто
                if not val and not any(c.isdigit() for c in value_str):
                     if not category: category = ocr_cell(cat_img, config=cell_config)
                     match = re.search(r'(\d+[\.,\s]\d+[\.,]\d+|\d+[\.,]\d+|\d+)', category)
                     if match: value_str = match.group(1)

                if not val:
                    val = parse_amount(value_str)
                if amount_is_plausible(val):
                    person_sum = val
                    log(f"Блок {block_num}: {name} -> {val} (OCR='{compact_text(value_str)}')")
                    # Обновляем кэш строки для следующих блоков
                    if cached_total_row == -1:
                        cached_total_row = row_idx
                        log(f"Строка ИТОГО К ВЫПЛАТЕ зафиксирована на индексе {cached_total_row}")
                    break # Нашли итоговую сумму, дальше по этой колонке не идем
                elif val:
                    log(f"Блок {block_num}: сумма отклонена как неправдоподобная: {val} (OCR='{compact_text(value_str)}')", "WARNING")
            
            if person_sum > 0:
                results.append((name, person_sum, block_num))
                log(f"Итого: {name} -> {person_sum}")
            else:
                log(f"ПРЕДУПРЕЖДЕНИЕ: Для {name} не найдена сумма в основной ячейке ИТОГО К ВЫПЛАТЕ.", "WARNING")
        
        results.sort(key=lambda x: x[2]) # Сортировка по block_num
        return [(r[0], r[1]) for r in results]
    except Exception as e:
        log(f"Ошибка при сеточном парсинге {image_path}: {e}", "ERROR")
        log(traceback.format_exc(), "DEBUG")
        return []

def main():
    reset_log()
    ensure_dependencies()
    log_runtime_info()
    tessdata_dir = ensure_rus_language()
    if tessdata_dir:
        os.environ['TESSDATA_PREFIX'] = tessdata_dir
        log(f"Установлен TESSDATA_PREFIX: {tessdata_dir}")
    
    # Ищем картинки в текущей папке
    extensions = ['*.jpg', '*.jpeg', '*.png']
    files = []
    for ext in extensions:
        files.extend(glob.glob(ext))
    
    if not files:
        print("Картинки не найдены в текущей директории.")
        return

    all_results = []
    log(f"Найдено файлов для обработки: {len(files)}")
    
    employee_dict = load_employees("employees.txt")
    if employee_dict:
        log(f"Загружен словарь сотрудников: {len(employee_dict)} имен.")

    files = sorted(files)
    for f in files:
        log(f"Обработка {f}...")
        data = parse_image(f, tessdata_dir, employee_dict)
        if data:
            all_results.extend(data)
    
    # Дедупликация (на случай одинаковых файлов в папке)
    unique_results = []
    seen = set()
    for item in all_results:
        if item not in seen:
            unique_results.append(item)
            seen.add(item)

    output_file = 'result.csv'
    try:
        # Убираем BOM, используем utf-8-sig для Excel
        with open(output_file, mode='w', encoding='utf-8-sig', newline='') as f_csv:
            writer = csv.writer(f_csv, delimiter=';')
            writer.writerow(['ФИО', 'Значение'])
            for name, value in unique_results:
                writer.writerow([name, value])
        log(f"Готово! Данные экспортированы в {output_file}. Всего строк: {len(unique_results)}")
        
        # Очистка временных файлов
        log("Очистка временных файлов...")
        for pattern in ["debug_*.txt", "img_*.jpg"]:
            for f in glob.glob(pattern):
                try: os.remove(f)
                except: pass
                
    except Exception as e:
        log(f"Ошибка при записи CSV: {e}", "ERROR")

if __name__ == "__main__":
    main()
