# 🎬 TUTORIAL PRÁTICO - Sua Primeira Venda Online

## 🎯 Objetivo
Gerar seu primeiro link de pagamento e testar uma venda completa.

---

## 📝 PASSO 1: Obter Credenciais (5 minutos)

### 1.1 Criar Conta de Desenvolvedor
1. Abra o navegador
2. Vá para: https://www.mercadopago.com.br/developers
3. Clique em **"Fazer login"**
4. Use sua conta Mercado Pago (ou crie uma nova)

### 1.2 Criar Aplicação
1. Clique em **"Suas integrações"**
2. Clique em **"Criar aplicação"**
3. Preencha:
   - Nome: `Galeria Digital Artes`
   - Descrição: `Sistema de vendas de obras de arte`
4. Clique em **"Criar"**

### 1.3 Copiar Token de Teste
1. Na página da aplicação, clique em **"Credenciais"**
2. Você verá duas seções:
   - **Credenciais de teste** (comece aqui)
   - Credenciais de produção (não use ainda)
3. Copie o **"Access Token"** de teste
   - Formato: `TEST-1234567890-XXXXXX-XXXXXXXXXXXXXXXX`
4. Guarde em algum lugar temporariamente

---

## 💻 PASSO 2: Configurar Projeto (3 minutos)

### 2.1 Abrir Projeto no VS Code
```powershell
cd c:\Users\pedro\Documents\qrCodeTelasExposicao\galeria-digital-artes
code .
```

### 2.2 Criar Arquivo .env
1. No VS Code, crie um novo arquivo chamado `.env`
2. Cole este conteúdo:

```env
MERCADO_PAGO_ACCESS_TOKEN_TEST=COLE_SEU_TOKEN_AQUI
ENVIRONMENT=test
BASE_URL=http://localhost:5000
```

3. Substitua `COLE_SEU_TOKEN_AQUI` pelo token que você copiou
4. Salve o arquivo (Ctrl + S)

### 2.3 Instalar Dependências
No terminal do VS Code:

```powershell
pip install python-dotenv mercadopago pandas
```

Aguarde a instalação completar (pode demorar ~1 minuto).

---

## 🚀 PASSO 3: Testar (2 minutos)

### 3.1 Executar Exemplo Simples
No terminal:

```powershell
python exemplo_simples.py
```

### 3.2 O que deve acontecer?
Você verá algo assim:

```
📤 Enviando para Mercado Pago...

✅ SUCESSO!
🔗 Link de pagamento: https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=123-abc...

💡 Cole este link no navegador para testar!
```

### 3.3 Testar o Link
1. Copie o link que apareceu
2. Cole no navegador
3. Você verá a página de checkout do Mercado Pago! 🎉

---

## 💳 PASSO 4: Fazer um Pagamento de Teste (5 minutos)

### 4.1 Na Tela de Checkout
1. Você verá: **"Obra de Arte - Teste"** por R$ 100,00
2. Clique em **"Pagar com cartão"**

### 4.2 Preencher Dados do Cartão FAKE
Use estes dados (são cartões de teste):

```
Número do cartão:  5031 4332 1540 6351
Vencimento:        12/25
CVV:               123
Nome no cartão:    APRO (nome especial para aprovar)
CPF:               12345678909
Email:             teste@teste.com
```

### 4.3 Finalizar
1. Clique em **"Pagar"**
2. Aguarde alguns segundos
3. Você será redirecionado para uma página de sucesso!

### 🎉 PARABÉNS!
Você acabou de processar seu primeiro pagamento via Mercado Pago!

**Importante:** Este foi um pagamento de TESTE. Nenhum dinheiro real foi cobrado.

---

## 🎨 PASSO 5: Criar Link para Obra Real (3 minutos)

Agora vamos criar um link para uma obra de verdade do catálogo.

### 5.1 Executar Script Completo
No terminal:

```powershell
python mercado_pago_api.py
```

### 5.2 O que acontece?
O script vai:
1. Carregar todas as 63 obras do CSV
2. Criar um link de pagamento para a Obra #1
3. Mostrar o resultado

Você verá:

```
🎨 SISTEMA DE PAGAMENTOS - GALERIA DIGITAL
==================================================
✅ 63 obras carregadas com sucesso!

📤 Criando preferência de pagamento para: PORTAS E JANELAS 1
💰 Valor: R$ 6000.00
🔢 Parcelamento: até 6x
✅ Preferência criada com sucesso!
🔗 Link de pagamento: https://...

✨ PARABÉNS! Link criado com sucesso!
🎨 Obra: PORTAS E JANELAS 1
💰 Valor: R$ 6000.00
```

### 5.3 Testar Este Link
1. Copie o link
2. Abra no navegador
3. Agora você verá a obra real com o preço real!

---

## 📊 PASSO 6: Gerar Links para TODAS as Obras (5 minutos)

### 6.1 Modificar o Script
1. Abra o arquivo `mercado_pago_api.py`
2. Vá até o final do arquivo (linha ~460)
3. Encontre estas linhas:

```python
# Exemplo 1: Criar link para uma obra específica
exemplo_uso_basico()

# Exemplo 2: Gerar links para todas as obras
# generate_all_payment_links()
```

4. Comente a primeira linha e descomente a segunda:

```python
# Exemplo 1: Criar link para uma obra específica
# exemplo_uso_basico()

# Exemplo 2: Gerar links para todas as obras
generate_all_payment_links()
```

5. Salve (Ctrl + S)

### 6.2 Executar
No terminal:

```powershell
python mercado_pago_api.py
```

### 6.3 O que acontece?
O script vai:
1. Processar TODAS as 63 obras
2. Criar um link de pagamento para cada uma
3. Salvar tudo em `obras_com_links_pagamento.csv`

Isso pode demorar ~1-2 minutos.

### 6.4 Ver Resultados
1. Abra o arquivo `obras_com_links_pagamento.csv`
2. Você verá:

```csv
ITEM,TELA,VALOR,PREFERENCE_ID,LINK_PAGAMENTO,STATUS
1,PORTAS E JANELAS 1,6000.0,123-abc...,https://...,SUCESSO
2,PORTAS E JANELAS 2,8400.0,456-def...,https://...,SUCESSO
...
```

---

## 🎯 PASSO 7: Integrar com seus QR Codes

Agora você tem links de pagamento para todas as obras!

### Opções de Uso

**Opção 1: Atualizar os HTMLs**
```html
<a href="LINK_DO_MERCADO_PAGO_AQUI" class="btn-comprar">
    Comprar Agora
</a>
```

**Opção 2: Gerar Novos QR Codes**
Use o `gerador_etiquetas.ipynb` com os novos links.

**Opção 3: Criar Página Intermediária**
```html
<!-- links_obras/item_1/index.html -->
<script>
    const linkPagamento = "LINK_DO_MERCADO_PAGO";
    // Redirecionar ou exibir informações
</script>
```

---

## 🔍 PASSO 8: Verificar Pagamentos no Dashboard

### 8.1 Acessar Dashboard
1. Vá para: https://www.mercadopago.com.br/activities
2. Faça login
3. Você verá todos os pagamentos (inclusive os testes)

### 8.2 Filtrar por Teste
1. Clique em **"Filtros"**
2. Selecione **"Modo sandbox"** ou **"Teste"**
3. Você verá apenas os pagamentos de teste

---

## 🎓 EXERCÍCIOS PRÁTICOS

### Exercício 1: Mudar Parcelamento
**Desafio:** Criar um link com 12 parcelas ao invés de 6.

**Dica:** Modifique a linha em `mercado_pago_api.py`:
```python
max_installments=12  # Era 6
```

### Exercício 2: Criar Link com Desconto
**Desafio:** Usar o valor com desconto PIX (coluna VALOR_PIX).

**Dica:** Em `ObrasManager.format_price()`, use `obra['VALOR_PIX']`.

### Exercício 3: Personalizar Descrição
**Desafio:** Adicionar mais informações na descrição da obra.

**Dica:** Modifique em `create_payment_preference()`:
```python
descricao = (
    f"{tecnica} | {dimensao} cm | Ano: {ano}\n"
    f"Artista: Paulo Canuto"
)
```

---

## ❓ TROUBLESHOOTING

### Erro: "Access Token não configurado"
**Solução:** 
1. Verifique se o arquivo `.env` existe
2. Confirme que o token está correto
3. Não esqueça das aspas: `MERCADO_PAGO_ACCESS_TOKEN_TEST=seu_token`

### Erro: "No module named 'mercadopago'"
**Solução:**
```powershell
pip install mercadopago
```

### Erro: "Arquivo dados_obras.csv não encontrado"
**Solução:** Execute o comando na pasta correta:
```powershell
cd c:\Users\pedro\Documents\qrCodeTelasExposicao\galeria-digital-artes
```

### Link não abre
**Solução:**
1. Verifique se está usando token de TESTE
2. Copie o link completo (sem quebras)
3. Teste em navegador anônimo/incógnito

### Pagamento não processa
**Solução:**
1. Use apenas cartões de teste oficiais
2. No nome, coloque "APRO" para aprovar
3. Veja mais cartões em: https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/additional-content/test-cards

---

## 🎯 CHECKLIST FINAL

Após completar este tutorial, você deve saber:

- [x] Criar conta no Mercado Pago Developers
- [x] Obter Access Token de teste
- [x] Configurar arquivo .env
- [x] Executar script Python
- [x] Gerar link de pagamento
- [x] Testar pagamento com cartão fake
- [x] Criar links para obras reais
- [x] Gerar links em lote
- [x] Ver pagamentos no dashboard

---

## 🚀 PRÓXIMO NÍVEL

Agora você está pronto para:

1. **Integrar no Frontend:** Adicionar botões de compra
2. **Implementar Webhooks:** Receber notificações automáticas
3. **Criar Dashboard:** Visualizar vendas e estatísticas
4. **Deploy Produção:** Colocar no ar com token real

Veja o arquivo `GUIA_MERCADO_PAGO.md` para continuar aprendendo!

---

**🎉 PARABÉNS! Você completou seu primeiro projeto backend!**

Agora você tem uma base sólida para construir sistemas de pagamento profissionais.

**Próximo desafio:** Crie um servidor Flask para automatizar este processo! 🚀
