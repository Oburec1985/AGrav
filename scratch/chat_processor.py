import json
import os
import re

# Набор ключевых слов для фильтрации (сигналы)
KEYWORDS = [
    "podkop", "zeroblock", "zapret", "goodbyedpi", "fragment", 
    "desync", "fake", "sni", "ttl", "hop", "quic", "http3", 
    "kyber", "nfqws", "tpws", "mtu", "mss"
]

def process_chat(json_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Loading {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    messages = data.get('messages', [])
    print(f"Found {len(messages)} messages. Filtering...")
    
    clusters = {kw: [] for kw in KEYWORDS}
    clusters['other_tech'] = []
    
    for msg in messages:
        text = ""
        if isinstance(msg.get('text'), str):
            text = msg['text']
        elif isinstance(msg.get('text'), list):
            for part in msg['text']:
                if isinstance(part, str):
                    text += part
                elif isinstance(part, dict) and 'text' in part:
                    text += part['text']
        
        text_lower = text.lower()
        
        found_kw = False
        for kw in KEYWORDS:
            if kw in text_lower:
                clusters[kw].append({
                    'date': msg.get('date'),
                    'from': msg.get('from'),
                    'text': text
                })
                found_kw = True
        
        # Если есть технические термины, но не из списка
        if not found_kw and re.search(r'config|settings|proxy|vpn|vless|reality', text_lower):
            clusters['other_tech'].append({
                 'date': msg.get('date'),
                 'from': msg.get('from'),
                 'text': text
            })

    # Сохраняем результаты по кластерам
    for kw, msgs in clusters.items():
        if not msgs:
            continue
        
        output_file = os.path.join(output_dir, f"{kw}_raw.md")
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(f"# Raw Extraction: {kw}\n\n")
            for m in msgs:
                out.write(f"**{m['date']} | {m['from']}**\n{m['text']}\n\n---\n\n")
        
    print("Extraction complete.")

if __name__ == "__main__":
    SOURCE = r"c:\Oburec\Antigravity\Projects\temp\ChatExport_2026-04-21\result.json"
    DEST = r"c:\Oburec\Antigravity\Projects\AGrav\scratch\raw_extraction"
    process_chat(SOURCE, DEST)
