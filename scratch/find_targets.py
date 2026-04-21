import os

ROOT_DIR = r"c:\Oburec\Antigravity\Projects\AGrav"

files_to_find = [
    "Навигация.md",
    "Стандарты_Разработки.md",
    "Path.md",
    "Домены_Знаний.md",
    "Метод_Парсинга_Книг.md",
    "Summary.md",
    "Локализация.md",
    "Стандарт_Логирования.md",
    "Память_и_Потоки.md",
    "EAV_Модель.md"
]

def find_files():
    found = {}
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file in files_to_find:
                if file not in found:
                    found[file] = []
                found[file].append(os.path.join(root, file))
    return found

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    results = find_files()
    for name, paths in results.items():
        print(f"File: {name}")
        for p in paths:
            print(f"  - {p}")
