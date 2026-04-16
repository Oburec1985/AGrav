import re
import os

filepath = r'c:\Oburec\Antigravity\Projects\AGrav\30_Библиотека\Книги\Modal_Testing\Modal_Testing.md'

PAGES = {
    4: "Шум и механические колебания: причины и следствия",
    6: "Анализ сигналов и анализ систем",
    7: "Отыскание причин проблем",
    9: "Приемы решения динамических проблем",
    11: "Анализ мод колебаний",
    12: "Математические динамические модели",
    13: "Применение данных мод колебаний",
    14: "Проверка аналитической математической модели",
    15: "Частотные характеристики",
    17: "Измерение подвижности — определения",
    18: "Оценки частотных характеристик (H1, H2)",
    21: "Функция когерентности",
    22: "Двухканальный анализатор (БПФ)",
    24: "Ошибки (случайные и систематические)",
    25: "Ошибка рассеяния (Leakage)",
    26: "Выбор оптимальной оценки (H1 vs H2)",
    27: "Возбуждение: Форма волны",
    28: "Управление спектром и Пик-фактор",
    29: "Способы возбуждения (Вибростенды и Молотки)",
    30: "Измерение силы и подсоединение вибростенда",
    31: "Измерение реакции: Датчики",
    32: "Крепление датчиков",
    33: "Нагрузка от датчиков на объект",
    34: "Случайное возбуждение",
    35: "Псевдослучайное возбуждение",
    36: "Ударное возбуждение: Теория",
    37: "Ударные молотки: Масса и жесткость",
    38: "Недостатки ударного возбуждения",
    39: "Ударные испытания и когерентность",
    40: "Методы взвешивания (Связь частота/время)",
    41: "Импульсная весовая функция и двойные удары",
    42: "Экспоненциальная весовая функция",
    43: "Сравнение различных видов возбуждения",
    44: "Калибровка системы",
    45: "Замечания по ударной калибровке",
    46: "Практический пример: Колебания портального крана",
    47: "Решение проблемы и выводы"
}

def clean_text(content):
    # This function joins lines that were broken by the PDF parser.
    # It identifies lines that should be joined based on the lack of ending punctuation.
    lines = content.split('\n')
    cleaned_lines = []
    buffer = ""

    for line in lines:
        s_line = line.strip()
        
        # Keep headers, images, and empty lines as they are
        if not s_line:
            if buffer:
                cleaned_lines.append(buffer.strip())
                buffer = ""
            cleaned_lines.append("")
            continue
            
        if s_line.startswith('#') or s_line.startswith('!') or s_line.startswith('---'):
            if buffer:
                cleaned_lines.append(buffer.strip())
                buffer = ""
            cleaned_lines.append(line)
            continue

        # Handle hyphenation at the end of the line
        if s_line.endswith('-'):
            buffer += s_line[:-1]
            continue
        
        # If the line ends with a "paragraph ending" punctuation, we might close the buffer.
        # But for books, it's better to join until a real break.
        # Let's check for typical sentence endings: . ! ? : ;
        buffer += s_line + " "
        
        if s_line[-1] in ".!?:;":
            # If the next line starts with a lowercase letter, it might still belong here? 
            # PDF usually breaks mid-sentence.
            pass

    if buffer:
        cleaned_lines.append(buffer.strip())

    return '\n'.join(cleaned_lines)

def beautify_headers(content):
    # Convert Page markers to descriptive anchors and headers
    def repl(match):
        pg_num = int(match.group(1))
        title = PAGES.get(pg_num, f"Страница {pg_num}")
        anchor = f"<a name=\"p{pg_num}\"></a>"
        return f"\n{anchor}\n## 🏷️ {title} (стр. {pg_num})\n\n[🔝 Сверху](#top)\n"
    
    # We need to handle headers that were potentially joined by clean_text
    return re.sub(r'## Page (\d+)', repl, content)

def insert_toc(content):
    toc = "# <a name=\"top\"></a>📗 Modal Testing: Модальный анализ\n\n"
    toc += "> [!IMPORTANT]\n"
    toc += "> В данном документе представлены основы модальных испытаний и измерений механической подвижности. "
    toc += "Анализ мод колебаний является эффективным средством моделирования динамического поведения конструкций.\n\n"
    
    toc += "## 📌 Оглавление\n\n"
    
    categories = {
        "📊 Введение и основы": [4, 6, 7, 9],
        "📐 Теория и модели": [11, 12, 13, 14, 15],
        "📉 Измерения и функции": [17, 18, 21, 22],
        "⚠️ Ошибки и точность": [24, 25, 26],
        "🔨 Возбуждение и датчики": [27, 28, 29, 30, 31, 32, 33],
        "⚡ Типы сигналов (Случайные/Ударные)": [34, 35, 36, 37, 38, 39],
        "⏳ Методы взвешивания (Windowing)": [40, 41, 42, 43],
        "⚙️ Калибровка и Практика": [44, 45, 46, 47]
    }
    
    for cat, pgs in categories.items():
        toc += f"### {cat}\n"
        for p in pgs:
            if p in PAGES:
                toc += f"- [{PAGES[p]} (стр. {p})](#p{p})\n"
        toc += "\n"
    
    toc += "---\n\n"
    return toc + content

def post_process_formatting(content):
    # Highlight specific terms
    content = content.replace("резонанс", "**резонанс**")
    content = content.replace("антирезонанс", "**антирезонанс**")
    content = content.replace("частотной характеристики", "**частотной характеристики**")
    content = content.replace("функция когерентности", "**функция когерентности**")
    content = content.replace("БПФ", "**БПФ**")
    
    # Add some premium callouts for definitions
    definitions = [
        ("Анализ сигналов", "Анализ сигналов представляет собой процесс определения откликов системы на неизвестное возбуждение."),
        ("Анализ систем", "Анализ систем является методом определения характерных свойств систем (отношение отклик/сила)."),
        ("H1 и H2", "Оценки H1 и H2 используются для минимизации влияния шумов на выходе и входе соответственно.")
    ]
    
    for term, definition in definitions:
        content = content.replace(definition, f"\n> [!TIP]\n> **{term}**: {definition}\n")

    return content

with open(filepath, 'r', encoding='utf-8') as f:
    orig_text = f.read()

# Strip existing TOC area if run multiple times
text = re.sub(r'^# .* Оглавление.*---', '', orig_text, flags=re.DOTALL)

text = clean_text(text)
text = beautify_headers(text)
text = post_process_formatting(text)
text = insert_toc(text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Beautification successful.")
