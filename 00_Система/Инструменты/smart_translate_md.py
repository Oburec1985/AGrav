import os
import sys
import argparse
import google.genai as genai
from google.genai import types
from tqdm import tqdm

def translate_chunk(client, text, model='gemini-1.5-flash'):
    """Отправляет фрагмент текста на интеллектуальный перевод."""
    prompt = f"""
    Ты - профессиональный технический переводчик с английского на русский.
    Твоя задача: перевести фрагмент Markdown документа, сохраняя ВСЮ разметку (заголовки, ссылки на картинки вида ![Asset...](...), якоря <a name="..."></a>).
    
    ТРЕБОВАНИЯ К ПЕРЕВОДУ:
    1. Используй корректную техническую терминологию:
       - Control Valve -> Регулирующий клапан
       - Actuator -> Привод (или Актуатор)
       - Trim -> Трим (внутренние детали клапана)
       - Stem -> Шток
       - Bonnet -> Крышка корпуса (или Боннет)
       - Dead Band -> Зона нечувствительности
       - Hysteresis -> Гистерезис
       - Setting point -> Уставка
       - Cavitation -> Кавитация
    2. Сохраняй стиль изложения: профессиональный, инженерный.
    3. Не переводи пути к файлам и ссылки.
    4. Если в тексте есть таблицы, переводи заголовки и содержимое ячеек, сохраняя структуру Markdown.
    
    ТЕКСТ ДЛЯ ПЕРЕВОДА:
    ---
    {text}
    ---
    """
    
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description="AGrav Smart MD Translator (Powered by Gemini)")
    parser.add_argument("input_md", help="Путь к исходному MD файлу")
    parser.add_argument("output_md", help="Путь для сохранения перевода")
    parser.add_argument("--api-key", required=True, help="Gemini API Key")
    parser.add_argument("--chunk-size", type=int, default=4000, help="Размер чанка в символах (по умолчанию 4000)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_md):
        print(f"Ошибка: Файл {args.input_md} не найден.")
        sys.exit(1)

    print(f"[*] Загрузка файла: {args.input_md}")
    with open(args.input_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Разбиение на чанки (по параграфам или строкам, чтобы не рвать на полуслове)
    lines = content.split('\n')
    chunks = []
    current_chunk = []
    current_len = 0
    
    for line in lines:
        if current_len + len(line) > args.chunk_size:
            chunks.append('\n'.join(current_chunk))
            current_chunk = [line]
            current_len = len(line)
        else:
            current_chunk.append(line)
            current_len += len(line)
    if current_chunk:
        chunks.append('\n'.join(current_chunk))

    print(f"[*] Подготовлено чанков для перевода: {len(chunks)}")
    client = genai.Client(api_key=args.api_key)
    
    translated_content = []
    for chunk in tqdm(chunks, desc="Перевод"):
        try:
            translated_text = translate_chunk(client, chunk)
            translated_content.append(translated_text)
        except Exception as e:
            print(f"\n[!] Ошибка при переводе чанка: {e}")
            translated_content.append(f"\n> [ОШИБКА ПЕРЕВОДА ФРАГМЕНТА]\n{chunk}")

    final_ru_md = '\n'.join(translated_content)
    
    with open(args.output_md, 'w', encoding='utf-8') as f:
        f.write(final_ru_md)
        
    print(f"\n[+] УСПЕХ: Перевод сохранен в {args.output_md}")

if __name__ == "__main__":
    main()
