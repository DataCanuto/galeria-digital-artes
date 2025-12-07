"""
Script para recriar os arquivos de redirecionamento com encoding UTF-8 correto
"""
import os

# Template HTML com encoding UTF-8
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=../../links_obras/item_{}/index.html">
    <title>Redirecionando...</title>
</head>
<body>
    <p>Redirecionando para a página da obra...</p>
    <p>Se não for redirecionado automaticamente, <a href="../../links_obras/item_{}/index.html">clique aqui</a>.</p>
</body>
</html>"""

# Criar 62 arquivos de redirecionamento
for i in range(1, 63):
    folder = f"qrcodes/item_{i}"
    os.makedirs(folder, exist_ok=True)
    
    filepath = os.path.join(folder, "index.html")
    content = html_template.format(i, i)
    
    # Salvar com encoding UTF-8 explícito
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Item {i}: {filepath}")

print(f"\n📊 Total: 62 arquivos de redirecionamento criados com UTF-8")
