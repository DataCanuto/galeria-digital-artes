# 🎓 CONCEITOS BACKEND - Explicados de Forma Simples

## 🌐 O que é Backend?

**Analogia do Restaurante:**
- **Frontend** = Salão do restaurante (o que o cliente vê)
- **Backend** = Cozinha (onde a mágica acontece)
- **API** = Garçom (leva pedidos e traz pratos)
- **Banco de Dados** = Despensa (onde os ingredientes ficam guardados)

No seu projeto:
- **Frontend:** HTML das obras (o cliente vê e clica)
- **Backend:** `mercado_pago_api.py` (processa o pagamento)
- **API:** Mercado Pago (intermedia entre você e o sistema de pagamento)
- **Banco de Dados:** `dados_obras.csv` (informações das obras)

---

## 🔑 Conceitos Fundamentais

### 1. API (Application Programming Interface)

**O que é?**
Uma forma de dois programas conversarem entre si.

**Exemplo Real:**
Quando você pede comida no iFood:
1. Você (Frontend) faz o pedido
2. iFood (API) envia para o restaurante
3. Restaurante (Backend) prepara
4. iFood (API) traz de volta a confirmação

**No Seu Código:**
```python
# Você fala com a API do Mercado Pago
response = sdk.preference().create(dados)

# Mercado Pago responde
if response["status"] == 201:
    link = response["response"]["init_point"]
```

---

### 2. REST API

**O que significa?**
- **RE**presentational **S**tate **T**ransfer
- Jeito padronizado de APIs conversarem

**Verbos HTTP:**
- `GET` - Pegar informação (como ler um livro)
- `POST` - Criar algo novo (como postar no Instagram)
- `PUT` - Atualizar (como editar um tweet)
- `DELETE` - Apagar (como excluir um email)

**Exemplo:**
```python
# GET - Buscar informação de um pagamento
sdk.payment().get(payment_id)

# POST - Criar uma preferência
sdk.preference().create(data)
```

---

### 3. JSON (JavaScript Object Notation)

**O que é?**
Formato de texto para trocar dados entre sistemas.

**Analogia:**
É como uma "ficha técnica" que todos entendem.

**Estrutura:**
```json
{
    "nome": "Pedro",
    "idade": 25,
    "hobbies": ["programar", "ler", "música"]
}
```

**No Seu Código:**
```python
preferencia = {
    "items": [
        {
            "title": "Obra de Arte",
            "price": 6000.00
        }
    ]
}
```

---

### 4. Autenticação (Access Token)

**O que é?**
Uma "carteirinha de identidade" para sua aplicação.

**Analogia:**
Como um cartão de sócio de clube:
- Você mostra na entrada
- O clube sabe quem você é
- Sabe quais áreas pode acessar

**No Código:**
```python
# Seu "cartão de sócio"
access_token = "TEST-123-abc..."

# Mostrando na "portaria" do Mercado Pago
sdk = mercadopago.SDK(access_token)
```

**Tipos:**
- **Bearer Token** - Tipo usado pelo Mercado Pago
- **API Key** - Chave simples
- **OAuth** - Sistema mais complexo

---

### 5. Webhook

**O que é?**
Uma "ligação automática" que o Mercado Pago te dá quando algo acontece.

**Analogia:**
Como notificações push do celular:
- Você não fica atualizando o app toda hora
- O app te avisa quando tem novidade

**Fluxo:**
```
1. Cliente paga no Mercado Pago
2. Mercado Pago processa
3. Mercado Pago "liga" para seu servidor (webhook)
4. Seu servidor atualiza o status do pedido
```

**Código (webhook_mercadopago.py):**
```python
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    if data['type'] == 'payment':
        payment_id = data['data']['id']
        # Buscar detalhes e processar
        
    return 'OK', 200
```

---

### 6. Ambiente de Teste vs Produção

**Teste (Sandbox):**
- Token começa com `TEST-`
- Não cobra dinheiro real
- Usa cartões fake
- Para desenvolver e testar

**Produção:**
- Token começa com `APP_USR-`
- Cobra dinheiro DE VERDADE
- Usa cartões reais
- Para vendas reais

**Analogia:**
- Teste = Ensaio de teatro
- Produção = Show ao vivo

---

### 7. Variáveis de Ambiente

**O que são?**
Configurações que mudam de acordo com onde o código roda.

**Por que usar?**
- **Segurança:** Credenciais não vão para o Git
- **Flexibilidade:** Muda teste/produção facilmente
- **Colaboração:** Cada dev tem suas próprias credenciais

**Arquivo .env:**
```env
# Desenvolvimento
ENVIRONMENT=test
DB_HOST=localhost

# Produção (outro arquivo)
ENVIRONMENT=prod
DB_HOST=servidor-prod.com
```

**No Código:**
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega o .env
token = os.getenv('MERCADO_PAGO_ACCESS_TOKEN_TEST')
```

---

### 8. OOP - Programação Orientada a Objetos

**O que é?**
Jeito de organizar código em "objetos" que têm características e comportamentos.

**Analogia:**
Uma classe é como uma planta de casa:
- **Classe:** Planta da casa
- **Objeto:** Casa construída
- **Atributos:** Cor, tamanho, quartos
- **Métodos:** Abrir porta, ligar luz

**No Seu Código:**
```python
class MercadoPagoPayment:
    # Atributos (características)
    def __init__(self, config):
        self.config = config
        self.sdk = config.get_sdk()
    
    # Métodos (ações)
    def create_payment_preference(self, item_number):
        # Lógica para criar pagamento
        pass
```

**Usando:**
```python
# "Construindo a casa"
mp = MercadoPagoPayment(config)

# "Usando a casa"
link = mp.create_payment_preference(1)
```

---

### 9. HTTP Status Codes

**O que são?**
Códigos que indicam se deu certo ou errado.

**Analogia:**
Como emojis de resposta:
- 😊 = Deu certo
- 😕 = Você errou
- 😱 = Servidor com problema

**Principais:**
- `200` - OK (deu certo)
- `201` - Created (criado com sucesso)
- `400` - Bad Request (você enviou dados errados)
- `401` - Unauthorized (credenciais inválidas)
- `404` - Not Found (não encontrado)
- `500` - Internal Server Error (problema no servidor)

**No Código:**
```python
if response["status"] == 201:
    print("✅ Criado com sucesso!")
elif response["status"] == 400:
    print("❌ Você enviou dados errados")
elif response["status"] == 401:
    print("❌ Token inválido")
```

---

### 10. Callback / Redirect URLs

**O que são?**
URLs para onde o cliente é enviado após o pagamento.

**Fluxo:**
```
Cliente → Mercado Pago → Paga → Redirect URL
```

**Tipos:**
```python
"back_urls": {
    "success": "https://seu-site.com/sucesso",  # Pagamento OK
    "failure": "https://seu-site.com/erro",     # Pagamento falhou
    "pending": "https://seu-site.com/pendente"  # Aguardando
}
```

**Exemplo de Página:**
```html
<!-- sucesso.html -->
<h1>🎉 Pagamento Aprovado!</h1>
<p>Obrigado pela compra!</p>
<p>ID do Pedido: <span id="order-id"></span></p>

<script>
    // Pega ID da URL
    const params = new URLSearchParams(window.location.search);
    const orderId = params.get('external_reference');
    document.getElementById('order-id').innerText = orderId;
</script>
```

---

## 🎯 Padrões de Design Usados no Projeto

### 1. Singleton (Config)
Uma única instância de configuração.

```python
class MercadoPagoConfig:
    def __init__(self):
        # Carrega apenas uma vez
        load_dotenv()
```

### 2. Factory (SDK Creation)
Cria objetos de forma padronizada.

```python
def get_sdk(self):
    return mercadopago.SDK(self.access_token)
```

### 3. Manager (ObrasManager)
Centraliza operações relacionadas.

```python
class ObrasManager:
    def get_obra_by_item(self, item):
        # Busca obra
    
    def format_price(self, price):
        # Formata preço
```

---

## 🛠️ Ferramentas do Desenvolvedor

### 1. Postman
Testa APIs sem escrever código.

**Como usar:**
1. Baixe: https://www.postman.com/
2. Crie uma requisição POST
3. URL: `https://api.mercadopago.com/checkout/preferences`
4. Headers: `Authorization: Bearer SEU_TOKEN`
5. Body: JSON da preferência
6. Enviar!

### 2. Python Interactive Shell
Testa código rapidamente.

```powershell
python
>>> from mercado_pago_api import MercadoPagoConfig
>>> config = MercadoPagoConfig()
>>> print(config.environment)
'test'
>>> exit()
```

### 3. Logs
Registra o que acontece.

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Preferência criada")
logger.error("Erro ao processar")
```

---

## 📊 Boas Práticas

### 1. Nunca Hardcode Credenciais
❌ **Errado:**
```python
token = "TEST-123-abc..."
```

✅ **Certo:**
```python
token = os.getenv('MERCADO_PAGO_ACCESS_TOKEN_TEST')
```

### 2. Valide Inputs
```python
def create_payment_preference(self, item_number):
    if not isinstance(item_number, int):
        raise TypeError("item_number deve ser um inteiro")
    
    if item_number < 1:
        raise ValueError("item_number deve ser positivo")
```

### 3. Trate Erros
```python
try:
    response = sdk.preference().create(data)
except Exception as e:
    logger.error(f"Erro ao criar preferência: {e}")
    return {"success": False, "error": str(e)}
```

### 4. Use Type Hints
```python
def format_price(self, price_str: str) -> float:
    return float(price_str.replace(',', '.'))
```

### 5. Docstrings
```python
def create_payment_preference(self, item_number: int) -> Dict:
    """
    Cria uma preferência de pagamento.
    
    Args:
        item_number: Número da obra
    
    Returns:
        Dicionário com resultado
    """
```

---

## 🚀 Conceitos Avançados (Para o Futuro)

### 1. Async/Await
Processar múltiplas coisas ao mesmo tempo.

```python
import asyncio

async def criar_multiplos_links():
    tasks = [criar_link(i) for i in range(1, 64)]
    return await asyncio.gather(*tasks)
```

### 2. Rate Limiting
Limitar quantas requisições por tempo.

```python
from time import sleep

for i in range(63):
    criar_link(i)
    sleep(0.5)  # Aguarda 0.5s entre cada
```

### 3. Caching
Guardar resultados para não calcular novamente.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_obra(item_number):
    # Busca obra (só executa 1x por item)
    return obra
```

### 4. Database
Salvar em banco de dados ao invés de CSV.

```python
import sqlite3

conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO pagamentos (item, valor, status)
    VALUES (?, ?, ?)
''', (1, 6000, 'approved'))
```

---

## 🎓 Recursos para Continuar Aprendendo

### Cursos Gratuitos
- **Python:** https://python.org/about/gettingstarted/
- **APIs REST:** https://restfulapi.net/
- **Flask:** https://flask.palletsprojects.com/tutorial/

### Livros
- "Python Fluente" - Luciano Ramalho
- "APIs RESTful com Flask" - Miguel Grinberg
- "Clean Code" - Robert C. Martin

### Prática
- **HackerRank:** https://www.hackerrank.com/
- **LeetCode:** https://leetcode.com/
- **Real Python:** https://realpython.com/

---

**🎉 Agora você entende os conceitos! Hora de praticar!**
