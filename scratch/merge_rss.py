import os
import shutil
from pathlib import Path

source_root = Path(r"c:\Oburec\Antigravity\Projects\temp\РСС")
dest_root = Path(r"c:\Oburec\Antigravity\Projects\AGrav")

mapping = {
    # 00_Система
    "Инструкции Obsidian": "00_Система/База_Знаний/Obsidian",
    "Модули": "00_Система/База_Знаний/Obsidian/Модули",
    "Плагины.md": "00_Система/База_Знаний/Obsidian/Плагины.md",
    "Альтернативы Обсидиан.md": "00_Система/База_Знаний/Obsidian/Альтернативы_Обсидиан.md",
    "Установка Obsidian.md": "00_Система/База_Знаний/Obsidian/Установка_Obsidian.md",
    "Горячие клавиши Obsidian.md": "00_Система/База_Знаний/Obsidian/Горячие_клавиши.md",
    "План работ по внедрению Obsidian.md": "00_Система/База_Знаний/Obsidian/План_внедрения.md",

    # 10_Работа - Датчики
    "Оборудование": "10_Работа/Датчики/Оборудование_РСС",
    "MR-114.md": "10_Работа/Датчики/MR-114.md",
    "MS-340.md": "10_Работа/Датчики/MS-340.md",
    "Таблица датчики.md": "10_Работа/Датчики/Таблица_датчики.md",

    # 10_Работа - Бизнес Процессы
    "ТКП": "10_Работа/Бизнес_Процессы/ТКП",
    "Бизнес процесс ТКП.md": "10_Работа/Бизнес_Процессы/Бизнес_процесс_ТКП.md",
    "Бизнес процессы.md": "10_Работа/Бизнес_Процессы/Бизнес_процессы.md",
    "Работа с договорами.md": "10_Работа/Бизнес_Процессы/Работа_с_договорами.md",

    # 10_Работа - Экспертиза
    "LLM_ИИ": "10_Работа/Экспертиза/ИИ",
    "ИИ_LLM.md": "10_Работа/Экспертиза/ИИ/ИИ_LLM.md",
    "Работа с Gemini CLI.md": "10_Работа/Экспертиза/ИИ/Работа_с_Gemini_CLI.md",
    "ДФМ (tip-timing и tip clearence).md": "10_Работа/Экспертиза/ДФМ.md",

    # 20_Проекты
    "Проекты": "20_Проекты/РСС/Проекты",
    "Рабочие": "20_Проекты/РСС/Рабочие",
    "ЛИАЗ": "20_Проекты/РСС/ЛИАЗ",
    "Сложность проекта.md": "20_Проекты/РСС/Сложность_проекта.md",
    "Запуск заказа.canvas": "20_Проекты/РСС/Запуск_заказа.canvas",
    "Шаблон заказа V02.canvas": "20_Проекты/РСС/Шаблон_заказа_V02.canvas",
    "ФБК 3251-ТКП.png": "20_Проекты/РСС/Ассеты/ФБК_3251-ТКП.png",
    "ФБК 3251.png": "20_Проекты/РСС/Ассеты/ФБК_3251.png",

    # 30_Библиотека
    "РСС Книга": "30_Библиотека/Книги/РСС_Книга",

    # 90_Архив
    "Тесты": "90_Архив/РСС_Черновики/Тесты",
    "черновики": "90_Архив/РСС_Черновики/черновики",
    "Untitled.md": "90_Архив/РСС_Черновики/Untitled.md",
    "текст для орг доработок.md": "90_Архив/РСС_Черновики/текст_для_орг_доработок.md",
    "Итоги 2025.md": "90_Архив/РСС_Итоги_2025.md",
}

# Остальные файлы (README, Оглавление и прочее) в корень проекта РСС в Архиве
archive_base = dest_root / "90_Архив" / "РСС_Контекст"
archive_base.mkdir(parents=True, exist_ok=True)

def safe_copy(src, dst):
    if not src.exists():
        print(f"[!] Warning: {src} does not exist.")
        return
    dst_path = Path(dst)
    if not dst_path.is_absolute():
        dst_path = dest_root / dst_path
    
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst_path.exists():
            print(f"[*] Merging dir: {src} -> {dst_path}")
            # Простое слияние содержимого
            for item in src.iterdir():
                safe_copy(item, dst_path / item.name)
        else:
            print(f"[+] Copying dir: {src} -> {dst_path}")
            shutil.copytree(src, dst_path)
    else:
        print(f"[+] Copying file: {src} -> {dst_path}")
        shutil.copy2(src, dst_path)

print("[*] Starting merge process...")

for src_name, dst_rel in mapping.items():
    safe_copy(source_root / src_name, dst_rel)

# Специальная обработка для оставшихся файлов
leftovers = ["README.md", "Оглавление.md", "Оглавление.xlsx", "Афоризмы.md", "Pasted image 20250815142753.png"]
for f in leftovers:
    safe_copy(source_root / f, archive_base / f"РСС_{f}")

print("[+] Merge completed.")
