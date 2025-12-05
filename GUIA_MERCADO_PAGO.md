# Integração com Mercado Pago - Guia de Configuração

## 🚀 O que foi implementado

### 1. **Geração de Links de Pagamento**
- Links de crédito (parcelamento em até 6x)
- Links de PIX (com 5% de desconto)
- Validação de status antes de gerar links

### 2. **Sistema de Webhook**
- Arquivo `webhook_mercadopago.py` para receber notificações
- Atualização automática de status quando pagamento aprovado
- Desativação de links após venda

### 3. **Interface HTML Atualizada**
- Mensagem de "OBRA VENDIDA" para itens indisponíveis
- Botões desabilitados para obras vendidas
- Verificação dinâmica de status

---

## 📋 Passos para Configurar

### **Passo 1: Obter Credenciais do Mercado Pago**

1. Acesse: https://www.mercadopago.com.br/developers/panel/credentials
2. Faça login com sua conta Mercado Pago
3. Copie o **Access Token de Teste** (começa com `TEST-`)
4. Para produção, use o **Access Token de Produção**

### **Passo 2: Configurar o Notebook**

Abra a **célula 12** do notebook `gerador_etiquetas.ipynb` e substitua:

```python
ACCESS_TOKEN = "TEST-SEU_ACCESS_TOKEN_AQUI"  # ← Cole seu token aqui
```

### **Passo 3: Instalar Dependências**

Execute no terminal:

```powershell
pip install mercadopago flask
```

### **Passo 4: Executar o Notebook**

Execute as células na seguinte ordem:

1. **Células 1-7**: Carregar dados e preparar DataFrame
2. **Célula 11**: Instalar SDK do Mercado Pago
3. **Célula 12**: Configurar credenciais
4. **Célula 13**: Definir funções de pagamento
5. **Célula 8**: Gerar links de pagamento para cada obra
6. **Célula 10**: Gerar páginas HTML com links integrados
7. **Célula 14**: Salvar CSV atualizado

### **Passo 5: Configurar Webhook (Opcional para Testes)**

Para receber notificações de pagamento em tempo real:

#### **Opção A: Teste Local (com ngrok)**

1. Instale o ngrok: https://ngrok.com/download
2. Execute o webhook:
   ```powershell
   python webhook_mercadopago.py
   ```
3. Em outro terminal, execute:
   ```powershell
   ngrok http 5000
   ```
4. Copie a URL gerada (ex: `https://abc123.ngrok.io`)
5. Atualize a célula 8 para incluir o webhook:
   ```python
   link_credito = criar_link_pagamento_credito(
       titulo=titulo,
       preco=preco,
       item_id=item_id,
       link_notificacao="https://abc123.ngrok.io/webhook/mercadopago"  # ← Adicione esta linha
   )
   ```

#### **Opção B: Produção (Heroku, Vercel, AWS)**

Hospede o arquivo `webhook_mercadopago.py` em um servidor web público e configure a URL nas preferences.

---

## 🔒 Como Funciona a Segurança

### **1. Validação de Status**
- Antes de gerar links, verifica se `status == 'disponível'`
- Obras vendidas recebem links `#indisponivel` ou `#vendido`

### **2. Pagamento Único**
- Quando um pagamento é aprovado, o webhook:
  1. Atualiza `status` para `'vendido'`
  2. Define `link_mp` e `link_pix` como `'#vendido'`
  3. Registra `data_hora` e `tipo_transacao`

### **3. Interface Bloqueada**
- HTML detecta status `'vendido'` e desabilita botões
- Mostra mensagem de "OBRA INDISPONÍVEL"
- JavaScript verifica status a cada 30 segundos

---

## 🧪 Testando o Sistema

### **Teste 1: Gerar Links**

Execute a célula 8 e verifique se os links foram criados:

```python
df[['item', 'telas', 'status', 'link_mp', 'link_pix']].head()
```

### **Teste 2: Webhook Local**

1. Execute o webhook:
   ```powershell
   python webhook_mercadopago.py
   ```
2. Teste o endpoint:
   ```powershell
   curl http://localhost:5000/webhook/test
   ```
3. Verifique status de uma obra:
   ```powershell
   curl http://localhost:5000/status/1
   ```

### **Teste 3: Pagamento de Teste**

1. Acesse um link de pagamento gerado
2. Use cartões de teste do Mercado Pago:
   - **VISA aprovado**: 4509 9535 6623 3704
   - **CVV**: 123
   - **Validade**: 11/25
   - **CPF**: 12345678909

3. Complete o pagamento
4. Verifique se o webhook atualizou o CSV:
   ```python
   df_atualizado = pd.read_csv("obras_com_links.csv")
   df_atualizado[df_atualizado['status'] == 'vendido']
   ```

---

## 📊 Estrutura do DataFrame

Após a execução completa, o DataFrame terá:

| Coluna | Descrição |
|--------|-----------|
| `item` | ID da obra |
| `telas` | Nome da obra |
| `status` | `'disponível'`, `'vendido'`, ou `'acervo pessoal'` |
| `link_mp` | Link de pagamento crédito (ou `'#vendido'`) |
| `link_pix` | Link de pagamento PIX (ou `'#vendido'`) |
| `data_hora` | Data/hora da venda (ISO 8601) |
| `tipo_transacao` | `'credito'` ou `'pix'` |

---

## ⚠️ Avisos Importantes

1. **Access Token**: NUNCA compartilhe publicamente. Use variáveis de ambiente em produção.
2. **Webhook URL**: Deve ser HTTPS em produção (exigência do Mercado Pago)
3. **CSV Backup**: Faça backup de `obras_com_links.csv` antes de executar
4. **Teste Primeiro**: Use credenciais de teste antes de ir para produção

---

## 🐛 Solução de Problemas

### **Erro: "SDK do Mercado Pago não encontrado"**
```powershell
pip install mercadopago
```

### **Erro: "Access Token inválido"**
- Verifique se copiou o token completo (começa com `TEST-`)
- Confirme que está usando o token correto (teste vs produção)

### **Links não estão sendo gerados**
- Verifique se `valor (r$)` e `valor_pix` não estão vazios
- Confirme formato dos valores (ex: "6.000,00")

### **Webhook não recebe notificações**
- Verifique se a URL é acessível publicamente
- Teste com `curl` ou Postman
- Veja logs em: https://www.mercadopago.com.br/developers/panel/webhooks

---

## 📞 Contato

Para dúvidas sobre integração com Mercado Pago:
- Documentação: https://www.mercadopago.com.br/developers
- Suporte: https://www.mercadopago.com.br/developers/pt/support

---

**Última atualização**: 05/12/2024
