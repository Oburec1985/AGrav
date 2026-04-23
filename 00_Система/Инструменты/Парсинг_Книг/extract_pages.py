import sys
import fitz
import os

def extract_pages(src_path, start_page, end_page, out_path):
    """Extract pages [start_page, end_page] (1-indexed) from src_path into out_path."""
    doc = fitz.open(src_path)
    if start_page < 1 or end_page > doc.page_count or start_page > end_page:
        raise ValueError('Invalid page range')
    new_doc = fitz.open()
    for p in range(start_page - 1, end_page):
        new_doc.insert_pdf(doc, from_page=p, to_page=p)
    new_doc.save(out_path)
    new_doc.close()
    doc.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python extract_pages.py <src_pdf> <start> <end> <out_pdf>')
        sys.exit(1)
    src, start, end, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    extract_pages(src, start, end, out)
    print(f'Extracted pages {start}-{end} to {out}')
