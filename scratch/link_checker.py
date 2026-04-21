import os
import re
from urllib.parse import unquote

ROOT_DIR = r"c:\Oburec\Antigravity\Projects\AGrav"

def find_links(content):
    # Matches [text](link)
    # This regex is specifically looking for markdown links
    return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

def check_links():
    broken_links = []
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # Try local windows encoding if utf-8 fails
                    try:
                        with open(file_path, 'r', encoding='cp1251') as f:
                            content = f.read()
                    except:
                        continue
                
                links = find_links(content)
                for text, link in links:
                    # Ignore web links
                    if link.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                        continue
                        
                    # Handle file:/// prefix
                    path_to_check = link
                    if path_to_check.startswith('file:///'):
                        path_to_check = path_to_check[8:]
                    
                    # Remove fragments
                    path_to_check = path_to_check.split('#')[0].split('?')[0]
                    
                    # Unquote URL encoding
                    path_to_check = unquote(path_to_check)
                    
                    # Normalize backslashes for Windows
                    path_to_check = path_to_check.replace('/', '\\')
                    
                    # Handle absolute paths
                    if os.path.isabs(path_to_check):
                        target = path_to_check
                    else:
                        # Relative path
                        target = os.path.normpath(os.path.join(root, path_to_check))
                    
                    if not os.path.exists(target):
                        broken_links.append((file_path, link, target))
    return broken_links

if __name__ == "__main__":
    import sys
    # Force output to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    results = check_links()
    if not results:
        print("No broken links found.")
    else:
        print(f"Found {len(results)} broken links:")
        for source, link, target in results:
            rel_source = os.path.relpath(source, ROOT_DIR)
            print(f"File: {rel_source}")
            print(f"  Link: {link}")
            print(f"  Target: {target}")
            print("-" * 20)
