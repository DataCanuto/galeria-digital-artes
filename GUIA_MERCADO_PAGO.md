# 🎓 GUIA DO ALUNO: Integração Mercado Pago

## 📋 ÍNDICE
1. [Obtendo Credenciais](#1-obtendo-credenciais)
2. [Configurando o Ambiente](#2-configurando-o-ambiente)
3. [Testando a Primeira Integração](#3-testando-a-primeira-integração)
4. [Entendendo o Código](#4-entendendo-o-código)
5. [Exercícios Práticos](#5-exercícios-práticos)

---

## 1. OBTENDO CREDENCIAIS

### Passo 1.1: Criar Conta no Mercado Pago Developers

1. Acesse: https://www.mercadopago.com.br/developers
2. Faça login com sua conta Mercado Pago (ou crie uma)
3. Vá em "Suas integrações" → "Criar aplicação"
4. Escolha um nome: "Galeria Digital Artes"

### Passo 1.2: Obter Access Token de TESTE

⚠️ **IMPORTANTE**: Comece sempre com o ambiente de TESTE!

1. No painel de desenvolvedores, vá em "Credenciais"
2. Copie o **Access Token de TESTE**
   - Formato: `TEST-1234567890-XXXXXX-XXXXXXXXXXXXXXXX`
3. Guarde esse token! Você vai precisar dele no próximo passo

### 📚 O que é Access Token?
É como uma "chave" que identifica sua aplicação no Mercado Pago.
- **Token de Teste**: Para desenvolver e testar (não cobra de verdade)
- **Token de Produção**: Para vendas reais (cobra de verdade)

---

## 2. CONFIGURANDO O AMBIENTE

### Passo 2.1: Instalar Dependências

Abra o terminal no VS Code e execute:

```powershell
pip install python-dotenv mercadopago pandas
```

### Passo 2.2: Criar Arquivo .env

1. Na raiz do projeto, crie um arquivo chamado `.env` (sem extensão)
2. Cole o seguinte conteúdo:

```env
# Credenciais de TESTE
MERCADO_PAGO_ACCESS_TOKEN_TEST=SEU_TOKEN_AQUI

# Ambiente atual
ENVIRONMENT=test

# URL base do seu site
BASE_URL=http://localhost:5000
```

3. Substitua `SEU_TOKEN_AQUI` pelo token que você copiou no Passo 1.2

### ⚠️ ATENÇÃO
- NUNCA compartilhe seu arquivo `.env`
- NUNCA faça commit do `.env` no Git
- O `.gitignore` já está protegendo você!

---

## 3. TESTANDO A PRIMEIRA INTEGRAÇÃO

### Passo 3.1: Executar o Exemplo Básico

No terminal, execute:

```powershell
python mercado_pago_api.py
```

### O que deve acontecer?

Você verá algo assim:

```
🎨 SISTEMA DE PAGAMENTOS - GALERIA DIGITAL
==================================================

==================================================
EXEMPLO: Criando link de pagamento para UMA obra
==================================================

✅ 63 obras carregadas com sucesso!

📤 Criando preferência de pagamento para: PORTAS E JANELAS 1
💰 Valor: R$ 6000.00
🔢 Parcelamento: até 6x
✅ Preferência criada com sucesso!
🆔 ID: 123456789-abc123...
🔗 Link de pagamento: https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=...

✨ PARABÉNS! Link criado com sucesso!
🎨 Obra: PORTAS E JANELAS 1
💰 Valor: R$ 6000.00

🔗 Compartilhe este link:
https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=...
```

### Passo 3.2: Testar o Link

1. Copie o link que apareceu
2. Cole no navegador
3. Você verá a tela de pagamento do Mercado Pago!

### 🧪 Cartões de Teste

Para testar pagamentos, use estes cartões FAKE:

**Cartão Aprovado:**
- Número: `5031 4332 1540 6351`
- Vencimento: qualquer data futura
- CVV: qualquer 3 dígitos
- Nome: qualquer nome

**Cartão Recusado:**
- Número: `5031 7557 3453 0604`

Mais cartões de teste: https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/additional-content/test-cards

---

## 4. ENTENDENDO O CÓDIGO

### 4.1: Estrutura de Classes

```python
MercadoPagoConfig
├── Gerencia credenciais
├── Seleciona ambiente (test/prod)
└── Cria SDK do Mercado Pago

ObrasManager
├── Carrega dados_obras.csv
├── Busca obra por número
└── Formata preços

MercadoPagoPayment
├── Cria preferências de pagamento
├── Configura parcelamento
└── Gera links de pagamento
```

### 4.2: Fluxo de Uma Venda

```
1. Cliente escaneia QR Code
   ↓
2. Seu site chama create_payment_preference()
   ↓
3. Mercado Pago retorna um link
   ↓
4. Cliente é redirecionado para o link
   ↓
5. Cliente paga com cartão
   ↓
6. Mercado Pago processa pagamento
   ↓
7. Cliente é redirecionado de volta (success/failure/pending)
```

### 4.3: O que é uma "Preferência"?

Uma preferência é um objeto JSON que você envia ao Mercado Pago com:

```python
{
    "items": [              # O que está sendo vendido
        {
            "title": "...",
            "price": 6000.00,
            "quantity": 1
        }
    ],
    "payment_methods": {    # Como aceitar pagamento
        "installments": 6   # Até 6 parcelas
    },
    "back_urls": {         # Para onde redirecionar
        "success": "...",
        "failure": "...",
        "pending": "..."
    }
}
```

---

## 5. EXERCÍCIOS PRÁTICOS

### Exercício 1: Criar Link para Obra Específica

Modifique `exemplo_uso_basico()` para criar um link da obra #5:

```python
resultado = mp_payment.create_payment_preference(
    item_number=5,  # Troque de 1 para 5
    max_installments=6
)
```

### Exercício 2: Mudar Parcelamento

Crie um link com 12 parcelas:

```python
resultado = mp_payment.create_payment_preference(
    item_number=1,
    max_installments=12  # Troque de 6 para 12
)
```

### Exercício 3: Gerar Links para Todas as Obras

No final do arquivo, descomente a linha:

```python
# generate_all_payment_links()  # Remova o #
```

Execute novamente. Isso criará um CSV com links de TODAS as obras!

### Exercício 4: Adicionar Desconto PIX

Modifique a classe `MercadoPagoPayment` para incluir desconto no PIX.

**Dica**: No CSV, já existe a coluna `VALOR_PIX` com 5% de desconto!

---

## 6. PRÓXIMOS PASSOS

### 6.1: Integrar com Flask (Servidor Web)

Crie rotas para:
- `/api/pagamento/<item_number>` - Gerar link
- `/pagamento/sucesso` - Página de confirmação
- `/pagamento/falha` - Página de erro

### 6.2: Webhook (Notificações)

Configure um webhook para receber notificações quando:
- Pagamento aprovado
- Pagamento cancelado
- Pagamento reembolsado

### 6.3: Banco de Dados

Salve os pagamentos em um banco de dados:
- ID da preferência
- Status do pagamento
- Dados do cliente
- Data/hora

---

## 📚 RECURSOS ADICIONAIS

### Documentação Oficial
- API Reference: https://www.mercadopago.com.br/developers/pt/reference
- Checkout Pro: https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/landing
- Python SDK: https://github.com/mercadopago/sdk-python

### Conceitos Importantes

**Preferência vs Pagamento**
- Preferência = "carrinho de compras" (o que você cria)
- Pagamento = transação real (o que o cliente faz)

**Ambientes**
- Sandbox/Test = Para testar sem cobrar
- Production = Para vendas reais

**Webhooks**
- Notificações automáticas do Mercado Pago
- Avisam quando algo acontece (pagamento, reembolso, etc.)

---

## 🆘 PROBLEMAS COMUNS

### Erro: "Access Token não configurado"
**Solução**: Verifique se o arquivo `.env` existe e tem o token correto

### Erro: "Arquivo dados_obras.csv não encontrado"
**Solução**: Execute o script na pasta raiz do projeto

### Link não abre
**Solução**: Certifique-se de estar usando o token de TESTE

### Cartão não é aceito
**Solução**: Use apenas cartões de teste da documentação oficial

---

## ✅ CHECKLIST DE APRENDIZADO

- [ ] Entendo o que é um Access Token
- [ ] Sei a diferença entre teste e produção
- [ ] Consigo gerar um link de pagamento
- [ ] Testei um pagamento com cartão fake
- [ ] Entendo o que é uma preferência
- [ ] Sei configurar parcelamento
- [ ] Consigo gerar links para múltiplas obras
- [ ] Entendo o fluxo completo de pagamento

---

**🎉 Parabéns! Você concluiu sua primeira integração backend!**

Próxima aula: Criando um servidor Flask para automatizar tudo isso! 🚀
