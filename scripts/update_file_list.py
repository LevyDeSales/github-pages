#!/usr/bin/env python3
import os
import re
import glob

def get_html_title(file_path):
    """Extrai o título do arquivo HTML ou usa o nome do arquivo se não encontrar."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                return title_match.group(1)
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
    
    # Se não conseguir extrair o título, usa o nome do arquivo
    return os.path.basename(file_path).replace('.html', '').replace('_', ' ')

def update_index_file():
    html_files = []
    
    # Encontra todos os arquivos HTML na pasta htmls
    for html_file in glob.glob('htmls/**/*.html', recursive=True):
        relative_path = html_file.replace('\\', '/')  # Para compatibilidade Windows
        title = get_html_title(html_file)
        html_files.append({
            'path': relative_path,
            'name': title
        })
    
    # Lê o arquivo index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Constrói o array JavaScript de arquivos
    js_array = []
    for file in html_files:
        js_array.append(f"                {{path: '{file['path']}', name: '{file['name']}'}}")
    
    js_list = ',\n'.join(js_array)
    
    # Insere a lista no index.html
    pattern = r'const htmlFiles = \[(.*?)\];'
    replacement = f'const htmlFiles = [\n{js_list}\n            ];'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Escreve o arquivo atualizado
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Lista atualizada com {len(html_files)} arquivos HTML")

if __name__ == "__main__":
    update_index_file() 