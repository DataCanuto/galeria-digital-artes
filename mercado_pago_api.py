"""Gerador de Links de Pagamento - Mercado Pago"""

import os
import sys
import mercadopago
from dotenv import load_dotenv
import pandas as pd
from typing import Dict

# ==============================================
# CONFIGURAÇÃO
# ==============================================

def get_mp_sdk():
    """Retorna SDK do Mercado Pago configurado"""
    load_dotenv()
    env = os.getenv('ENVIRONMENT', 'test')
    token = os.getenv(f'MERCADO_PAGO_ACCESS_TOKEN_{env.upper()}')
    
    if not token:
        raise ValueError("❌ Token não configurado no .env")
    
    return mercadopago.SDK(token)


# ==============================================
# GERAÇÃO DE LINKS
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


def generate_fake_payment_links(item_number: int, valor: float) -> Dict:
    """Gera links fake para desenvolvimento"""
    fake_id = f"TEST-PREF-{item_number:04d}"
    return {
        "success": True,
        "preference_id": fake_id,
        "link_mp": f"https://mpago.la/test/{fake_id}",
        "valor": valor,
        "mode": "TEST"
    }


def create_real_payment_link(df_row: Dict, sdk) -> Dict:
    """Cria link real via API Mercado Pago"""
    titulo = df_row.get('telas', '')
    preco = float(df_row.get('valor (r$)', 0))
    parcelas = int(df_row.get('op_parcelamento', 6))
    
    preference_data = {
        "items": [{
            "title": titulo,
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": preco
        }],
        "payment_methods": {
            "installments": parcelas
        },
        "external_reference": f"OBRA_{df_row.get('item')}",
        "statement_descriptor": "GALERIA DIGITAL"
    }
    
    response = sdk.preference().create(preference_data)
    
    if response["status"] in [200, 201]:
        link = response["response"].get('init_point') or response["response"].get('sandbox_init_point')
        return {"success": True, "payment_link": link}
    else:
        return {"success": False, "error": response}


def generate_all_payment_links(mode: str = 'test', csv_path: str = 'dados_obras.csv'):
    """Gera links para todas as obras e retorna lista de links"""
    print(f"🔗 MODO: {mode.upper()}")
    print("=" * 60)
    
    # Carrega CSV
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.lower()
        df['valor (r$)'] = df['valor (r$)'].apply(limpar_valor_brasileiro)
        
        # Extrair op_parcelamento
        import re
        df['op_parcelamento'] = df['parcelamento'].apply(
            lambda x: re.search(r'/\s*(\d+)', str(x)).group(1) if pd.notna(x) and re.search(r'/\s*(\d+)', str(x)) else '6'
        )
        
        print(f"✅ {len(df)} obras carregadas")
    except FileNotFoundError:
        print(f"❌ {csv_path} não encontrado!")
        return []
    
    # Inicializa SDK se for produção
    sdk = get_mp_sdk() if mode == 'prod' else None
    
    sucesso = 0
    erros = 0
    links_mp = []
    
    # Processa cada obra
    for index, row in df.iterrows():
        item = row['item']
        valor = row['valor (r$)']
        
        if valor == 0:
            print(f"⏭️  Item {item}: Acervo pessoal")
            links_mp.append(None)
            continue
        
        try:
            if mode == 'test':
                result = generate_fake_payment_links(item, valor)
                links_mp.append(result['link_mp'])
                print(f"✅ Item {item}: {result['link_mp']}")
                sucesso += 1
            else:
                result = create_real_payment_link(row.to_dict(), sdk)
                if result['success']:
                    links_mp.append(result['payment_link'])
                    print(f"✅ Item {item}: {result['payment_link']}")
                    sucesso += 1
                else:
                    print(f"❌ Item {item}: Erro")
                    links_mp.append(None)
                    erros += 1
        except Exception as e:
            print(f"❌ Item {item}: {str(e)}")
            links_mp.append(None)
            erros += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Sucesso: {sucesso} | Erros: {erros}")
    print(f"📋 Total de links gerados: {len([l for l in links_mp if l])}")
    
    # Salvar CSV com links para o notebook usar
    df['link_mp'] = links_mp
    output_path = csv_path.replace('dados_obras.csv', 'obras_com_links_api.csv')
    df.to_csv(output_path, index=False)
    print(f"💾 Links salvos em: {output_path}")
    print("=" * 60)
    
    return links_mp


# ==============================================
# EXECUÇÃO
# ==============================================

if __name__ == "__main__":
    if '--mode' in sys.argv:
        idx = sys.argv.index('--mode') + 1
        mode = sys.argv[idx] if idx < len(sys.argv) else 'test'
        generate_all_payment_links(mode=mode)
    else:
        print("USO:")
        print("  python mercado_pago_api_clean.py --mode test")
        print("  python mercado_pago_api_clean.py --mode prod")
