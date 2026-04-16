import os
import shutil
import re
from pathlib import Path
from collections import defaultdict

vault_root = Path(r"c:\Oburec\Antigravity\Projects\AGrav")
work_dir = vault_root / "10_Работа"
sensors_dir = work_dir / "Датчики"
equip_dir = work_dir / "Оборудование"

# 1. Ensure new structure exists
mera_dir = equip_dir / "Измерительное" / "Mera"
gt_dir = equip_dir / "Датчики" / "GlobalTest"

mera_dir.mkdir(parents=True, exist_ok=True)
gt_dir.mkdir(parents=True, exist_ok=True)

print("[*] Transitioning files to new hierarchy...")

# 2. Perform Moves
move_map = [
    # Mera equipment
    (sensors_dir / "Модули" / "MR-114.md", mera_dir / "MR-114.md"),
    (sensors_dir / "Оборудование" / "MS-340.md", mera_dir / "MS-340.md"),
    
    # GlobalTest subtree
    (sensors_dir / "Notes", gt_dir / "Notes"),
    (sensors_dir / "Attachments", gt_dir / "Attachments"),
    (sensors_dir / "Каталог_Датчиков.md", gt_dir / "Каталог_Датчиков.md"),
    (sensors_dir / "Таблица_датчики.md", gt_dir / "Таблица_датчики.md"),
]

for src, dst in move_map:
    if src.exists():
        if dst.exists():
            if dst.is_dir():
                shutil.rmtree(dst)
            else:
                dst.unlink()
        shutil.move(str(src), str(dst))
        print(f"  [Move] {src.name} -> {dst.parent.relative_to(vault_root)}")

# Cleanup duplicates/folders
dup = sensors_dir / "Оборудование_РСС" / "MS-340.md"
if dup.exists():
    dup.unlink()
    print(f"  [Del] Duplicate: {dup.relative_to(vault_root)}")

# Remove old Sensors tree if empty (or specific parts of it)
shutil.rmtree(sensors_dir, ignore_errors=True)
print("[+] Physical move complete.")

# 3. Mass Link Repair (Phase 2)
print("[*] Starting vault-wide link restoration...")

vault_index = defaultdict(list)
for f in vault_root.rglob("*"):
    if f.is_file():
        rel_p = f.relative_to(vault_root).as_posix()
        vault_index[f.name.lower()].append(rel_p)
        if f.suffix.lower() == ".md":
            vault_index[f.stem.lower()].append(rel_p)

md_link_re = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
wiki_link_re = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

md_files = list(vault_root.rglob("*.md")) + list(vault_root.rglob("*.canvas"))

stats = {"fixed": 0, "verified": 0, "broken_still": 0}

for md_file in md_files:
    try:
        content = md_file.read_text(encoding="utf-8")
    except: continue
    orig = content

    def fix_md(match):
        label, link = match.groups()
        clean = link.split("#")[0].strip()
        if not clean or clean.startswith(("http", "mailto", "tel:", "file:///")): return match.group(0)
        
        if (md_file.parent / clean).exists():
            stats["verified"] += 1
            return match.group(0)
            
        basename = Path(clean).name.lower()
        candidates = vault_index.get(basename) or vault_index.get(basename + ".md")
        if candidates:
            stats["fixed"] += 1
            return f"[[{Path(candidates[0]).name}]]"
        return match.group(0)

    def fix_wiki(match):
        target_full = match.group(1)
        clean = target_full.split("#")[0].strip()
        if not clean: return match.group(0)
        
        if (vault_root / clean).exists() or (md_file.parent / clean).exists():
            stats["verified"] += 1
            return match.group(0)
            
        basename = clean.split("/")[-1].split("\\")[-1].lower()
        candidates = vault_index.get(basename) or vault_index.get(basename + ".md")
        if candidates:
            stats["fixed"] += 1
            return match.group(0).replace(target_full, Path(candidates[0]).name)
        return match.group(0)

    content = md_link_re.sub(fix_md, content)
    content = wiki_link_re.sub(fix_wiki, content)
    
    if content != orig:
        md_file.write_text(content, encoding="utf-8")

print(f"[*] Link restoration done. Stats: {stats}")
