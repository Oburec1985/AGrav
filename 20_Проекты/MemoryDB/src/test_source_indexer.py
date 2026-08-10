import tempfile
import unittest
from pathlib import Path

from src.source_indexer import chunk_source, read_source


class SourceIndexerTests(unittest.TestCase):
    def test_cp1251_source_is_decoded(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy.cpp"
            path.write_bytes("// Проверка\nint value = 1;".encode("cp1251"))
            self.assertIn("Проверка", read_source(path))

    def test_chunks_have_line_ranges_and_overlap(self):
        text = "\n".join(f"line {index}" for index in range(1, 31))
        chunks = chunk_source(text, max_lines=10, overlap=2)
        self.assertEqual((1, 10),
                         (chunks[0]["line_start"], chunks[0]["line_end"]))
        self.assertEqual(9, chunks[1]["line_start"])
        self.assertEqual(30, chunks[-1]["line_end"])

    def test_symbol_is_extracted(self):
        chunks = chunk_source("class CRecorderCore\n{\n};")
        self.assertEqual("CRecorderCore", chunks[0]["symbol"])


if __name__ == "__main__":
    unittest.main()
