"""Gerador de Links de Pagamento PIX - Mercado Pago"""

import os
import sys
import requests
from dotenv import load_dotenv
import pandas as pd
from typing import Dict

# ==============================================
# CONFIGURAÇÃO
# ==============================================

def get_access_token():
    """Retorna access token do Mercado Pago"""
    load_dotenv()
    env = os.getenv('ENVIRONMENT', 'test')
    token = os.getenv(f'MERCADO_PAGO_ACCESS_TOKEN_{env.upper()}')
    
    if not token:
        raise ValueError("❌ Token não configurado no .env")
    
    return token


# ==============================================
# GERAÇÃO DE LINKS PIX
# ==============================================

def limpar_valor_brasileiro(valor):
    """Converte valores no formato brasileiro para float"""
    if pd.isna(valor):
        return 0.0
    
    valor_str = str(valor).strip().lower()
    
    if valor_str in ['acervo pessoal', '', 'nan', '-', '  -   ']:
        return 0.0
    
    valor_str = valor_str.replace(' ', '')
    
    if ',' in valor_str:
        valor_str = valor_str.replace('.', '')
        valor_str = valor_str.replace(',', '.')
    
    try:
        valor_float = float(valor_str)
        if valor_float > 100000:
            valor_float = valor_float / 100
        return round(valor_float, 2)
    except:
        return 0.0


def generate_fake_pix_links(item_number: int, valor: float) -> Dict:
    """Gera links fake para desenvolvimento (PIX)"""
    fake_id = f"TEST-PIX-{item_number:04d}"
    return {
        "success": True,
        "preference_id": fake_id,
        "link_mp_pix": f"https://mpago.la/test/pix/{fake_id}",
        "valor": valor,
        "mode": "TEST"
    }


def create_real_pix_link(df_row: Dict, access_token: str) -> Dict:
    """Cria link real PIX via API REST do Mercado Pago"""
    titulo = df_row.get('telas', '')
    preco_pix = float(df_row.get('valor_pix', 0))
    item_id = df_row.get('item')
    
    # URL da API de Preferences
    url = "https://api.mercadopago.com/checkout/preferences"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "items": [{
            "title": f"{titulo} - PIX (5% desconto)",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": preco_pix
        }],
        "payment_methods": {
            "excluded_payment_methods": [
                {"id": "visa"},
                {"id": "master"},
                {"id": "amex"},
                {"id": "elo"},
                {"id": "hipercard"},
                {"id": "naranja"},
                {"id": "cabal"}
            ],
            "excluded_payment_types": [
                {"id": "credit_card"},
                {"id": "debit_card"},
                {"id": "ticket"},
                {"id": "atm"},
                {"id": "prepaid_card"}
            ],
            "installments": 1
        },
        "back_urls": {
            "success": f"https://datacanuto.github.io/galeria-digital-artes/links_obras/item_{item_id}/index.html?status=success",
            "failure": f"https://datacanuto.github.io/galeria-digital-artes/links_obras/item_{item_id}/index.html?status=failure",
            "pending": f"https://datacanuto.github.io/galeria-digital-artes/links_obras/item_{item_id}/index.html?status=pending"
        },
        "auto_return": "approved",
        "external_reference": f"OBRA_{item_id}_PIX",
        "statement_descriptor": "GALERIA DIGITAL",
        "expires": False,
        "purpose": "onboarding_credits"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code in [200, 201]:
            data = response.json()
            link = data.get('init_point', data.get('sandbox_init_point'))
            return {"success": True, "payment_link": link}
        else:
            return {"success": False, "error": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}


def generate_all_pix_links(mode: str = 'test', csv_path: str = 'dados_obras.csv'):
    """Gera links PIX para todas as obras e retorna lista de links"""
    print(f"🔗 MODO PIX: {mode.upper()}")
    print("=" * 60)
    
    # Carrega CSV
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.lower()
        df['valor (r$)'] = df['valor (r$)'].apply(limpar_valor_brasileiro)
        df['valor_pix'] = df['valor_pix'].apply(limpar_valor_brasileiro)
        
        print(f"✅ {len(df)} obras carregadas")
    except FileNotFoundError:
        print(f"❌ {csv_path} não encontrado!")
        return []
    
    # Inicializa token se for produção
    access_token = get_access_token() if mode == 'prod' else None
    
    sucesso = 0
    erros = 0
    links_mp_pix = []
    
    # Processa cada obra
    for index, row in df.iterrows():
        item = row['item']
        valor = row['valor (r$)']
        valor_pix = row['valor_pix']
        
        if valor == 0:
            print(f"⏭️  Item {item}: Acervo pessoal")
            links_mp_pix.append(None)
            continue
        
        try:
            if mode == 'test':
                result = generate_fake_pix_links(item, valor_pix)
                links_mp_pix.append(result['link_mp_pix'])
                print(f"✅ Item {item}: {result['link_mp_pix']}")
                sucesso += 1
            else:
                result = create_real_pix_link(row.to_dict(), access_token)
                if result['success']:
                    links_mp_pix.append(result['payment_link'])
                    print(f"✅ Item {item}: {result['payment_link']}")
                    sucesso += 1
                else:
                    print(f"❌ Item {item}: Erro")
                    links_mp_pix.append(None)
                    erros += 1
        except Exception as e:
            print(f"❌ Item {item}: {str(e)}")
            links_mp_pix.append(None)
            erros += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Sucesso: {sucesso} | Erros: {erros}")
    print(f"📋 Total de links PIX gerados: {len([l for l in links_mp_pix if l])}")
    
    # Salvar CSV com links PIX para o notebook usar
    df['link_mp_pix'] = links_mp_pix
    output_path = csv_path.replace('dados_obras.csv', 'obras_com_links_pix_api.csv')
    df.to_csv(output_path, index=False)
    print(f"💾 Links PIX salvos em: {output_path}")
    print("=" * 60)
    
    return links_mp_pix


# ==============================================
# MAIN
# ==============================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Gera links de pagamento PIX via Mercado Pago')
    parser.add_argument('--mode', choices=['test', 'prod'], default='test', 
                        help='test = links fake | prod = API real')
    parser.add_argument('--csv', default='dados_obras.csv', 
                        help='Caminho do CSV com dados das obras')
    
    args = parser.parse_args()
    
    links = generate_all_pix_links(mode=args.mode, csv_path=args.csv)
    
    if not links:
        sys.exit(1)
