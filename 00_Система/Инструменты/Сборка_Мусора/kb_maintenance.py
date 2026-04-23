import os
import re
import hashlib
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Oburec\Antigravity\Projects\AGrav")
MD_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+\.md)\)")
OBSIDIAN_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

def get_file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def audit():
    """Только аудит. Никаких изменений файлов."""
    md_files = list(ROOT.rglob("*.md"))
    all_files_by_name = defaultdict(list)
    for f in ROOT.rglob("*"):
        if f.is_file():
            all_files_by_name[f.name].append(f)
    
    broken_links = []
    duplicates = defaultdict(list)
    
    # 1. Поиск дубликатов
    hashes = {}
    for f in ROOT.rglob("*"):
        if f.is_file() and ".git" not in str(f) and ".obsidian" not in str(f):
            try:
                h = get_file_hash(f)
                if h in hashes:
                    duplicates[h].append(str(f))
                else:
                    hashes[h] = str(f)
            except: continue
    
    # 2. Проверка ссылок
    for md in md_files:
        if ".git" in str(md) or ".obsidian" in str(md): continue
        try:
            with open(md, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for target in MD_PATTERN.findall(content):
                    if target.startswith("http"): continue
                    t_path = (md.parent / target).resolve()
                    if not t_path.exists():
                        broken_links.append((str(md), target))
                for target in OBSIDIAN_PATTERN.findall(content):
                    target_name = os.path.basename(target)
                    if "." not in target_name: target_name += ".md"
                    if target_name not in all_files_by_name:
                        broken_links.append((str(md), f"[[{target}]]"))
        except: continue

    report_path = ROOT / "scratch" / "audit_report.txt"
    with open(report_path, "w", encoding="utf-8") as rep:
        rep.write(f"BROKEN LINKS ({len(broken_links)}):\n")
        for src, link in broken_links:
            rep.write(f"{src} -> {link}\n")
        rep.write(f"\nDUPLICATES ({len(duplicates)} sets):\n")
        for h, paths in duplicates.items():
            rep.write(f"Hash {h}:\n  - {hashes[h]}\n")
            for p in paths: rep.write(f"  - {p}\n")
    
    print(f"Audit complete. Report saved to {report_path}")

if __name__ == "__main__":
    audit()
