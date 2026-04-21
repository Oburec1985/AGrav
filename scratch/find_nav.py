import os

ROOT_DIR = r"c:\Oburec\Antigravity\Projects\AGrav"

def find_missing():
    targets = ["Навигация.md", "Домены_Знаний.md"]
    found = {}
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file in targets:
                found[file] = os.path.join(root, file)
    return found

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    res = find_missing()
    print(res)
