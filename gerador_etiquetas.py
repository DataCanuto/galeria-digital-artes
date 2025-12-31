# gerador_etiquetas.py
# Script para gerar etiquetas HTML para obras, com preço, parcelamento e botão de WhatsApp

import os
import pandas as pd
import numpy as np
import urllib.parse
import qrcode
import re

# Definir constantes para caminhos e URLs
URL_BASE_QR = "https://datacanuto.github.io/galeria-digital-artes"
DIRETORIO_BASE = r'D:\Documentos\REPOSITÓRIO-LOCAL\GaleriaDigital'
IMG_PATH = os.path.join(DIRETORIO_BASE, "galeria-digital-artes", "assets", "img")
DIRETORIO_SAIDA = os.path.join(DIRETORIO_BASE, "galeria-digital-artes", "links_obras")
QR_EXPORT_DIR = os.path.join(DIRETORIO_BASE, "galeria-digital-artes", "qr_codes_export")
DADOS = os.path.join(DIRETORIO_BASE, "dados_obras.csv")
TEMPLATE_OBRA = os.path.join(DIRETORIO_BASE, "galeria-digital-artes", "assets", "template_obra.html")

os.makedirs(QR_EXPORT_DIR, exist_ok=True)

# Carregar template HTML
with open(TEMPLATE_OBRA, 'r', encoding='utf-8') as f:
    template_obra = f.read()

# Carregar dados
print("Lendo dados...")
df = pd.read_csv(DADOS)
df.columns = df.columns.str.strip().str.lower()

# Mapear imagens
img_list = os.listdir(IMG_PATH)
img_dict = {i+1: img for i, img in enumerate(img_list)}
df['fotos'] = df['item'].map(img_dict)

def gerar_html_obra(row):
    titulo = row.get('telas', '')
    titulo_encoded = urllib.parse.quote(str(titulo))
    tecnica_dimensao_ano = f"{row.get('técnica', '')}, {row.get('dimensão', '')}, {row.get('ano','')}"
    preco = row.get('valor (r$)', 0)
    preco_str = f"R$ {preco}" if preco else "Sob consulta"
    parcelamento = row.get('parcelamento', '')
    parcelamento_str = f"{parcelamento} SEM JUROS" if parcelamento else ""
    html = template_obra.replace('{{TITULO}}', titulo) \
                        .replace('{{FOTO}}', row.get('fotos', '')) \
                        .replace('{{TECNICA_DIMENSAO_ANO}}', tecnica_dimensao_ano) \
                        .replace('{{TITULO_ENCODED}}', titulo_encoded) \
                        .replace('{{URL_BASE}}', URL_BASE_QR) \
                        .replace('{{PRECO}}', preco_str) \
                        .replace('{{PARCELAMENTO}}', parcelamento_str)
    return html

def gerar_qrcode(link, caminho_salvar):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    imagem_qr = qr.make_image(fill_color="black", back_color="white")
    imagem_qr.save(caminho_salvar)

# Gerar etiquetas
for i, row in df.iterrows():
    idx_val = int(row.get('item', i))
    pasta = f"item_{idx_val}"
    caminho_pasta = os.path.join(DIRETORIO_SAIDA, pasta)
    os.makedirs(caminho_pasta, exist_ok=True)
    link_final = f"{URL_BASE_QR}/links_obras/{pasta}/index.html"
    # Gerar e salvar HTML
    html_content = gerar_html_obra(row)
    with open(os.path.join(caminho_pasta, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    # Gerar QR codes
    gerar_qrcode(link_final, os.path.join(caminho_pasta, "qrcode.png"))
    qr_export_nome = f"qr_{idx_val}.png"
    gerar_qrcode(link_final, os.path.join(QR_EXPORT_DIR, qr_export_nome))

print("✅ Etiquetas e QR Codes gerados com sucesso!")
