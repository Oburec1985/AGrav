import os
import shutil
from pathlib import Path

# Mapping based on exact FullNames found in the previous listing
moves = [
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Инструкции Obsidian", r"C:\Oburec\Antigravity\Projects\AGrav\00_Система\База_Знаний\Obsidian"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Модули", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Датчики\Модули"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Оборудование", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Датчики\Оборудование"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Тесты\Таблица датчики.md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Датчики\Таблица_датчики.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Глоссарий\Бизнес процесс ТКП.md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Бизнес_Процессы\Бизнес_процесс_ТКП.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Глоссарий\Бизнес процессы.md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Бизнес_Процессы\Бизнес_процессы.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Глоссарий\Перечень стендов.md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Бизнес_Процессы\Перечень_стендов.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Рабочие\Работа с договорами.md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Бизнес_Процессы\Работа_с_договорами.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Проекты\LLM_ИИ", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Экспертиза\ИИ"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Проекты\ДФМ (tip-timing и tip clearence).md", r"C:\Oburec\Antigravity\Projects\AGrav\10_Работа\Экспертиза\ДФМ.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\ТКП\ЛИАЗ", r"C:\Oburec\Antigravity\Projects\AGrav\20_Проекты\РСС\ЛИАЗ"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга\Рабочие", r"C:\Oburec\Antigravity\Projects\AGrav\20_Проекты\РСС\Рабочие"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\ФБК 3251-ТКП.png", r"C:\Oburec\Antigravity\Projects\AGrav\20_Проекты\РСС\Ассеты\ФБК_3251-ТКП.png"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\ФБК 3251.png", r"C:\Oburec\Antigravity\Projects\AGrav\20_Проекты\РСС\Ассеты\ФБК_3251.png"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\РСС Книга", r"C:\Oburec\Antigravity\Projects\AGrav\30_Библиотека\Книги\РСС_Книга"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Тесты", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Черновики\Тесты"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\черновики", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Черновики\черновики"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\README.md", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Контекст\РСС_README.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Оглавление.md", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Контекст\РСС_Оглавление.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Оглавление.xlsx", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Контекст\РСС_Оглавление.xlsx"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Афоризмы.md", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Контекст\РСС_Афоризмы.md"),
    (r"C:\Oburec\Antigravity\Projects\temp\РСС\Pasted image 20250815142753.png", r"C:\Oburec\Antigravity\Projects\AGrav\90_Архив\РСС_Контекст\РСС_Pasted_image.png"),
]

def safe_merge(src_str, dst_str):
    src = Path(src_str)
    dst = Path(dst_str)
    if not src.exists():
        print(f"Skipping (not found): {src}")
        return
    
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    if src.is_dir():
        if dst.exists():
            print(f"Merging dir: {src}")
            for item in src.iterdir():
                safe_merge(item, dst / item.name)
        else:
            print(f"Moving dir: {src}")
            shutil.move(str(src), str(dst))
    else:
        print(f"Moving file: {src}")
        if dst.exists():
            os.remove(dst)
        shutil.move(str(src), str(dst))

for s, d in moves:
    try:
        safe_merge(s, d)
    except Exception as e:
        print(f"Error moving {s}: {e}")

print("Merge done.")
