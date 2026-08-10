import hashlib
import os
import re
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, List

from src.config import ORIGINAL_RECORDER_DIRS, ORIGINAL_RECORDER_ROOT
from src.database import MemoryDatabase


SOURCE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx",
    ".idl", ".odl", ".pas", ".inc", ".rc", ".def"
}
EXCLUDE_DIRS = {
    ".git", ".svn", "debug", "release", "x64", "win32", "lib", "obj",
    "build", "cmake-build-debug", "cmake-build-release", "generated"
}
MAX_FILE_BYTES = 2 * 1024 * 1024
SOURCE_NAMESPACE = uuid.UUID("47df89ad-880d-4e02-a2c8-65fa98ab17c2")


def read_source(path: Path) -> str:
    """Read legacy text without ever modifying the original source file."""
    data = path.read_bytes()
    if len(data) > MAX_FILE_BYTES or b"\x00" in data:
        raise ValueError("binary or oversized source")
    for encoding in ("utf-8-sig", "utf-8", "cp1251", "cp866", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def chunk_source(text: str, max_lines: int = 90,
                 overlap: int = 12) -> List[Dict[str, Any]]:
    """Split code into overlapping, line-addressable chunks."""
    lines = text.splitlines()
    chunks = []
    start = 0
    symbol_pattern = re.compile(
        r"^\s*(?:class|struct|interface|enum|namespace|procedure|function|"
        r"constructor|destructor)\s+([\w:~]+)", re.IGNORECASE)
    cpp_function = re.compile(
        r"^\s*[\w:<>,~*&\s]+\s+([\w:~]+)\s*\([^;]*\)\s*"
        r"(?:const\s*)?\{?\s*$")
    while start < len(lines):
        end = min(len(lines), start + max_lines)
        block = lines[start:end]
        symbol = ""
        for line in block:
            match = symbol_pattern.match(line) or cpp_function.match(line)
            if match:
                symbol = match.group(1)
                break
        chunks.append({
            "line_start": start + 1,
            "line_end": end,
            "symbol": symbol,
            "text": "\n".join(block),
        })
        if end == len(lines):
            break
        start = max(start + 1, end - overlap)
    return chunks


class SourceIndexer:
    def __init__(self, db: MemoryDatabase):
        self.db = db

    def iter_original_recorder_files(self) -> Iterable[Path]:
        root = ORIGINAL_RECORDER_ROOT.resolve()
        for directory in ORIGINAL_RECORDER_DIRS:
            scan_root = root / directory
            if not scan_root.exists():
                continue
            for current, dirs, files in os.walk(scan_root):
                dirs[:] = [item for item in dirs
                            if item.lower() not in EXCLUDE_DIRS]
                for name in files:
                    path = Path(current) / name
                    if path.suffix.lower() in SOURCE_EXTENSIONS:
                        yield path

    def sync_original_recorder(self, dry_run: bool = False) -> Dict[str, int]:
        root = ORIGINAL_RECORDER_ROOT.resolve()
        indexed = self.db.get_all_indexed_source_ids("original-recorder")
        active = set()
        stats = {"created": 0, "updated": 0, "skipped": 0,
                 "deleted": 0, "errors": 0}
        for path in self.iter_original_recorder_files():
            relative = path.resolve().relative_to(root).as_posix()
            source_id = str(uuid.uuid5(
                SOURCE_NAMESPACE, f"original-recorder:{relative.lower()}"))
            active.add(source_id)
            try:
                text = read_source(path)
                digest = hashlib.sha256(
                    text.encode("utf-8", errors="replace")).hexdigest()
                exists = source_id in indexed
                if exists and self.db.source_hash(source_id) == digest:
                    stats["skipped"] += 1
                    continue
                key = "updated" if exists else "created"
                if not dry_run:
                    self.db.save_source_chunks(
                        source_id=source_id,
                        file_path=str(path.resolve()),
                        content_hash=digest,
                        chunks=chunk_source(text),
                        project_context="original-recorder",
                        source_kind="original-recorder")
                stats[key] += 1
            except Exception as exc:
                stats["errors"] += 1
                print(f"[SOURCE ERROR] {path}: {exc}")
        for source_id in set(indexed) - active:
            if not dry_run:
                self.db.delete_source_chunks(source_id)
            stats["deleted"] += 1
        return stats


if __name__ == "__main__":
    print(SourceIndexer(MemoryDatabase()).sync_original_recorder())
