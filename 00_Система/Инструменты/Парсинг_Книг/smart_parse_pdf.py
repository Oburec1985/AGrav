import os
import re
import sys
import argparse
import fitz  # PyMuPDF для нарезка чанков
import google.genai as genai
from google.genai import types

# Глобальный счетчик изображений для сквозной нумерации при чанках
GLOBAL_IMAGE_COUNT = 0

def clean_text_formatting(md_text):
    """Очистка артефактов переноса строк."""
    line_break_regex = re.compile(r'(\w)\n([а-яёa-z])')
    return line_break_regex.sub(r'\1 \2', md_text)

def parse_with_docling_chunk(pdf_path, output_dir, start_page_num=1):
    """
    Парсинг чанка PDF через Docling.
    start_page_num — физический номер первой страницы этого чанка в книге.
    """
    global GLOBAL_IMAGE_COUNT
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling_core.types.doc import DocItemLabel
    
    attachments_dir = os.path.join(output_dir, "Attachments")
    if not os.path.exists(attachments_dir):
        os.makedirs(attachments_dir)

    pipeline_options = PdfPipelineOptions()
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    pipeline_options.images_scale = 3.0  # Увеличенное разрешение (300+ DPI эквивалент)
    pipeline_options.do_ocr = True 
    pipeline_options.do_table_structure = True 
    
    converter = DocumentConverter(
        allowed_formats=[InputFormat.PDF],
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    result = converter.convert(pdf_path)
    doc = result.document
    
    md_lines = []
    last_page = -1
    
    for item, level in doc.iterate_items():
        # Считаем реальный номер страницы в книге
        current_rel_page = item.prov[0].page_no if item.prov else last_page
        real_page_no = current_rel_page + start_page_num - 1
        
        if current_rel_page != last_page and current_rel_page > 0:
            md_lines.append(f'\n---\n<a name="p{real_page_no}"></a>')
            md_lines.append(f'## 🏷️ Страница {real_page_no}')
            md_lines.append('[🔝 Сверху](#top)\n')
            last_page = current_rel_page

        # Таблицы
        if item.label == DocItemLabel.TABLE:
            md_lines.append("\n### 📊 Таблица\n")
            try:
                if hasattr(item, "export_to_markdown"):
                    md_lines.append(item.export_to_markdown())
                else:
                    md_lines.append("> [Таблица]")
            except:
                md_lines.append("> [Ошибка рендеринга таблицы]")
        
        # Картинки и формулы
        elif item.label in [DocItemLabel.PICTURE, DocItemLabel.FORMULA, DocItemLabel.CHART]:
            GLOBAL_IMAGE_COUNT += 1
            image_filename = f"asset_p{real_page_no}_{GLOBAL_IMAGE_COUNT}.png"
            image_save_path = os.path.join(attachments_dir, image_filename)
            
            saved = False
            if hasattr(item, "image") and item.image:
                item.image.pil_image.save(image_save_path)
                saved = True
            
            if saved:
                md_lines.append(f"\n![Asset {GLOBAL_IMAGE_COUNT}](Attachments/{image_filename})\n")
            elif hasattr(item, "text") and item.text:
                md_lines.append(f"\n${item.text}$\n")
        
        # Текст и заголовки
        elif item.label in [DocItemLabel.TEXT, DocItemLabel.PARAGRAPH, DocItemLabel.SECTION_HEADER, DocItemLabel.TITLE]:
            if hasattr(item, "text") and item.text:
                text = item.text.strip()
                if text.isdigit() and len(text) < 4: continue
                
                if item.label in [DocItemLabel.SECTION_HEADER, DocItemLabel.TITLE]:
                    h_level = max(2, level) if item.label == DocItemLabel.SECTION_HEADER else 1
                    md_lines.append(f"\n{'#' * h_level} {text}\n")
                else:
                    md_lines.append(text)
        
        if md_lines and md_lines[-1] != "": md_lines.append("")

    return "\n".join(md_lines)

def process_adaptive(pdf_path, output_dir, chunk_size=10):
    """Адаптивный парсинг с разбиением на чанки для экономии RAM."""
    print(f"[!] Вход в адаптивный режим (пакеты по {chunk_size} стр.)")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    full_md = ['<a name="top"></a>\n# ' + os.path.basename(pdf_path).replace('.pdf', '')]
    
    temp_dir = os.path.join(output_dir, "temp_chunks")
    if not os.path.exists(temp_dir): os.makedirs(temp_dir)
    
    for start in range(0, total_pages, chunk_size):
        end = min(start + chunk_size, total_pages)
        chunk_pdf_path = os.path.join(temp_dir, f"chunk_{start}_{end}.pdf")
        
        chunk_doc = fitz.open()
        chunk_doc.insert_pdf(doc, from_page=start, to_page=end-1)
        chunk_doc.save(chunk_pdf_path)
        chunk_doc.close()
        
        try:
            chunk_md = parse_with_docling_chunk(chunk_pdf_path, output_dir, start_page_num=start+1)
            full_md.append(chunk_md)
        except Exception as e:
            print(f"[!] Ошибка при обработке чанка {start}-{end}: {e}")
        
        os.remove(chunk_pdf_path)
        
    final_content = "\n".join(full_md)
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    output_filename = os.path.basename(pdf_path).replace('.pdf', '_smart.md')
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    try: os.rmdir(temp_dir)
    except: pass
    
    print(f"\n[+] УСПЕХ: Книга спарсена (страниц: {total_pages})")
    print(f"[+] Итоговый файл: {output_path}")
    doc.close()

def parse_with_gemini(pdf_path, output_dir, api_key):
    """Парсинг через Gemini 1.5 Flash (Cloud AI)."""
    print(f"[*] Запуск Gemini AI для {pdf_path}...")
    client = genai.Client(api_key=api_key)
    file_info = client.files.upload(file=pdf_path)
    
    prompt = "Преобразуй этот PDF в Markdown. Сохрани таблицы и формулы. Расставь якоря <a name='p{номер}'></a>."
    
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=[
            types.Content(parts=[
                types.Part.from_uri(file_uri=file_info.uri, mime_type=file_info.mime_type),
                types.Part.from_text(text=prompt)
            ])
        ]
    )
    
    output_path = os.path.join(output_dir, os.path.basename(pdf_path).replace('.pdf', '_ai.md'))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"[+] AI-парсинг завершен: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="AGrav Ultimate Smart Parser")
    parser.add_argument("pdf_path", help="Путь к PDF")
    parser.add_argument("output_dir", help="Папка выхода")
    parser.add_argument("--mode", choices=["docling", "gemini"], default="docling")
    parser.add_argument("--api-key", help="API-ключ Gemini")
    parser.add_argument("--chunk-size", type=int, default=10, help="Размер чанка (по умолчанию 10)")
    
    args = parser.parse_args()
    if not os.path.exists(args.output_dir): os.makedirs(args.output_dir)
    
    if args.mode == "docling":
        process_adaptive(args.pdf_path, args.output_dir, chunk_size=args.chunk_size)
    else:
        if not args.api_key:
            print("Ошибка: нужен --api-key")
            sys.exit(1)
        parse_with_gemini(args.pdf_path, args.output_dir, args.api_key)

if __name__ == "__main__":
    main()
