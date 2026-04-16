import fitz  # PyMuPDF
import os
import re

def parse_pdf_to_md(pdf_path, output_dir):
    """
    Автоматизированный парсинг PDF в Markdown с извлечением изображений.
    Стандарт AGrav.
    """
    attachments_dir = os.path.join(output_dir, "Attachments")
    if not os.path.exists(attachments_dir):
        os.makedirs(attachments_dir)

    doc = fitz.open(pdf_path)
    md_content = f"# {os.path.basename(pdf_path).replace('.pdf', '')}\n\n"
    
    # Регулярка для склеивания разорванных строк (line breaks)
    # Ищет символ \n, за которым следует маленькая буква
    line_break_regex = re.compile(r'(\w)\n([а-яёa-z])')

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        # Базовая очистка текста
        clean_text = line_break_regex.sub(r'\1 \2', text)
        
        md_content += f"<a name=\"p{page_num + 1}\"></a>\n"
        md_content += f"## 🏷️ Страница {page_num + 1}\n\n"
        md_content += "[🔝 Сверху](#top)\n\n"
        md_content += clean_text + "\n\n"
        
        # Извлечение изображений
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"image_p{page_num+1}_{img_index}.{image_ext}"
            image_save_path = os.path.join(attachments_dir, image_filename)
            
            with open(image_save_path, "wb") as f:
                f.write(image_bytes)
                
            md_content += f"![Image {img_index}](Attachments/{image_filename})\n\n"
    
    output_path = os.path.join(output_dir, f"{os.path.basename(pdf_path).replace('.pdf', '')}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    doc.close()
    print(f"Парсинг завершен. Файл: {output_path}")

if __name__ == "__main__":
    # Пример использования (можно запустить напрямую или импортировать)
    import sys
    if len(sys.argv) > 2:
        parse_pdf_to_md(sys.argv[1], sys.argv[2])
    else:
        print("Использование: python parse_pdf.py <путь_к_pdf> <папка_вывода>")
