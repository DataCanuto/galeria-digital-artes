"""
Webhook para receber notificações de pagamento do Mercado Pago
Este arquivo deve ser hospedado em um servidor web acessível publicamente

Para testar localmente, use ngrok:
1. Instale: pip install pyngrok
2. Execute: ngrok http 5000
3. Use a URL gerada como notification_url nas preferences

Para produção, hospede em: Heroku, Vercel, AWS Lambda, etc.
"""

from flask import Flask, request, jsonify
import mercadopago
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

# Configurações
ACCESS_TOKEN = "TEST-SEU_ACCESS_TOKEN_AQUI"
CSV_PATH = "obras_com_links.csv"

sdk = mercadopago.SDK(ACCESS_TOKEN)


def atualizar_status_obra(external_reference, payment_info):
    """
    Atualiza o status da obra no CSV quando um pagamento é aprovado
    
    Args:
        external_reference: Referência no formato "obra_{item_id}_{tipo}"
        payment_info: Dicionário com informações do pagamento
    """
    try:
        # Carregar CSV
        df = pd.read_csv(CSV_PATH)
        
        # Extrair item_id da referência (formato: obra_1_credito ou obra_1_pix)
        parts = external_reference.split('_')
        if len(parts) >= 2:
            item_id = int(parts[1])
            tipo_pagamento = parts[2] if len(parts) > 2 else 'desconhecido'
        else:
            print(f"Formato de referência inválido: {external_reference}")
            return False
        
        # Localizar a obra no DataFrame
        idx = df[df['item'] == item_id].index
        
        if len(idx) == 0:
            print(f"Obra {item_id} não encontrada no CSV")
            return False
        
        idx = idx[0]
        status_atual = df.at[idx, 'status']
        
        # Verificar se já foi vendida
        if status_atual == 'vendido':
            print(f"Obra {item_id} já foi vendida anteriormente")
            return False
        
        # Atualizar status da obra
        df.at[idx, 'status'] = 'vendido'
        df.at[idx, 'data_hora'] = payment_info.get('date_approved', datetime.now().isoformat())
        df.at[idx, 'tipo_transacao'] = tipo_pagamento
        
        # Desativar links de pagamento
        df.at[idx, 'link_mp'] = '#vendido'
        df.at[idx, 'link_pix'] = '#vendido'
        
        # Salvar CSV atualizado
        df.to_csv(CSV_PATH, index=False, encoding='utf-8')
        
        print(f"✅ Obra {item_id} marcada como VENDIDA via {tipo_pagamento}")
        print(f"   Data: {payment_info.get('date_approved')}")
        print(f"   Valor: R$ {payment_info.get('transaction_amount')}")
        
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar status da obra: {e}")
        return False


@app.route('/webhook/mercadopago', methods=['POST'])
def webhook():
    """
    Endpoint para receber notificações do Mercado Pago
    """
    try:
        # Receber dados da notificação
        data = request.get_json()
        
        print(f"📩 Notificação recebida: {data}")
        
        # Verificar tipo de notificação
        if data.get('type') == 'payment':
            payment_id = data.get('data', {}).get('id')
            
            if payment_id:
                # Buscar informações completas do pagamento
                payment_info = sdk.payment().get(payment_id)
                payment = payment_info["response"]
                
                print(f"💳 Pagamento ID: {payment_id}")
                print(f"   Status: {payment.get('status')}")
                print(f"   Valor: R$ {payment.get('transaction_amount')}")
                
                # Verificar se o pagamento foi aprovado
                if payment.get('status') == 'approved':
                    external_reference = payment.get('external_reference')
                    
                    if external_reference:
                        # Atualizar status da obra
                        sucesso = atualizar_status_obra(external_reference, payment)
                        
                        if sucesso:
                            return jsonify({
                                'status': 'success',
                                'message': 'Obra atualizada com sucesso'
                            }), 200
                        else:
                            return jsonify({
                                'status': 'error',
                                'message': 'Erro ao atualizar obra'
                            }), 500
        
        # Retornar 200 OK para todas as notificações
        return jsonify({'status': 'received'}), 200
        
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/webhook/test', methods=['GET'])
def test():
    """Endpoint de teste para verificar se o webhook está funcionando"""
    return jsonify({
        'status': 'online',
        'message': 'Webhook do Mercado Pago funcionando!',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/status/<int:item_id>', methods=['GET'])
def check_status(item_id):
    """Endpoint para verificar o status de uma obra específica"""
    try:
        df = pd.read_csv(CSV_PATH)
        obra = df[df['item'] == item_id]
        
        if len(obra) == 0:
            return jsonify({'error': 'Obra não encontrada'}), 404
        
        obra_data = obra.iloc[0]
        return jsonify({
            'item': int(obra_data['item']),
            'titulo': obra_data['telas'],
            'status': obra_data['status'],
            'data_venda': obra_data.get('data_hora', ''),
            'tipo_transacao': obra_data.get('tipo_transacao', '')
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("🚀 Iniciando servidor webhook do Mercado Pago...")
    print(f"📂 CSV: {CSV_PATH}")
    print(f"🌐 Acesse: http://localhost:5000/webhook/test")
    app.run(debug=True, host='0.0.0.0', port=5000)
