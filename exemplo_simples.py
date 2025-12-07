"""
Script de exemplo simples para testar a integração com Mercado Pago.

Este é um exemplo MÍNIMO para você entender o básico.
Depois de dominar este, explore o mercado_pago_api.py completo.
"""

import mercadopago
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Pega o token de acesso
access_token = os.getenv('MERCADO_PAGO_ACCESS_TOKEN_TEST')

if not access_token:
    print("❌ ERRO: Configure o arquivo .env primeiro!")
    print("Veja o arquivo .env.example")
    exit()

# Cria o SDK do Mercado Pago
sdk = mercadopago.SDK(access_token)

# Define o que você quer vender
preferencia = {
    "items": [
        {
            "title": "Obra de Arte - Teste",
            "description": "Pintura acrílica sobre tela",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 100.00  # R$ 100,00
        }
    ],
    "back_urls": {
        "success": "http://localhost:5000/sucesso",
        "failure": "http://localhost:5000/falha",
        "pending": "http://localhost:5000/pendente"
    }
}

# Cria a preferência no Mercado Pago
print("📤 Enviando para Mercado Pago...")
resposta = sdk.preference().create(preferencia)

# Verifica se deu certo
if resposta["status"] == 201:
    link = resposta["response"]["init_point"]
    print("\n✅ SUCESSO!")
    print(f"🔗 Link de pagamento: {link}")
    print("\n💡 Cole este link no navegador para testar!")
else:
    print("\n❌ ERRO:")
    print(resposta)
