# 🎨 Galeria Digital & QR Code System - Paulo Canuto

Sistema completo de **Galeria Digital Interativa** para exposição de artes com integração de pagamentos via Mercado Pago.

## 📋 Visão Geral

Este projeto conecta obras físicas ao ambiente digital através de QR Codes, permitindo:
- 🖼️ Visualização detalhada das obras
- 💳 Compra direta com cartão de crédito (Mercado Pago)
- 📱 Contato via WhatsApp
- 🏷️ Geração automática de etiquetas e QR Codes

## ✨ Funcionalidades

### Frontend
- **Catálogo Digital**: Páginas individuais para cada obra com design responsivo
- **Integração de Pagamento**: Links diretos para checkout do Mercado Pago
- **Contato Direto**: Botões de WhatsApp para negociação
- **QR Codes**: Acesso rápido via mobile durante a exposição

### Backend (Novo! 🎉)
- **API Mercado Pago**: Geração automática de links de pagamento
- **Gestão de Obras**: Sistema de gerenciamento de dados das obras
- **Automação**: Scripts Python para processar e gerar conteúdo
- **Webhooks**: Notificações de pagamento em tempo real

## 🛠 Tecnologias

### Frontend
- HTML5 & CSS3
- JavaScript (Vanilla)
- GitHub Pages (Hospedagem)

### Backend
- **Python 3.8+**
- **Mercado Pago SDK** - Integração de pagamentos
- **Pandas** - Processamento de dados
- **Flask** - Servidor web (webhooks)
- **QRCode** - Geração de QR codes
- **Jupyter Notebook** - Análise e experimentação

## 🚀 Quick Start

### 1. Clonar Repositório
```bash
git clone https://github.com/DataCanuto/galeria-digital-artes.git
cd galeria-digital-artes
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar Credenciais

Crie um arquivo `.env` na raiz do projeto:
```env
MERCADO_PAGO_ACCESS_TOKEN_TEST=SEU_TOKEN_TESTE
ENVIRONMENT=test
BASE_URL=http://localhost:5000
```

**Como obter o token:**
1. Acesse https://www.mercadopago.com.br/developers
2. Crie uma aplicação
3. Copie o Access Token de TESTE

### 4. Testar Integração
```bash
python mercado_pago_api.py
```

## 📚 Documentação

- **[GUIA_MERCADO_PAGO.md](GUIA_MERCADO_PAGO.md)** - Tutorial completo de integração (recomendado para iniciantes)
- **[QUICK_START.md](QUICK_START.md)** - Referência rápida
- **[mercado_pago_api.py](mercado_pago_api.py)** - Código comentado linha por linha

## 📂 Estrutura do Projeto

```
galeria-digital-artes/
├── dados_obras.csv              # Dados das obras de arte
├── mercado_pago_api.py          # API Mercado Pago (NOVO!)
├── webhook_mercadopago.py       # Servidor de webhooks
├── gerador_etiquetas.ipynb      # Gerador de QR codes e etiquetas
├── index.html                   # Página principal
├── catalog_mobile/              # Catálogo mobile
├── links_obras/                 # Páginas individuais das obras
│   ├── item_1/
│   ├── item_2/
│   └── ...
├── assets/
│   ├── css/
│   └── img/
└── qr_codes_export/            # QR codes gerados

## 🎓 Aprendendo Backend com Este Projeto

Este projeto é ideal para quem está começando no backend! O código está estruturado como uma **aula prática**:

### Conceitos Abordados
1. **APIs RESTful**: Integração com API externa (Mercado Pago)
2. **Variáveis de Ambiente**: Proteção de credenciais sensíveis
3. **POO (Programação Orientada a Objetos)**: Classes e organização de código
4. **Processamento de Dados**: Pandas para manipular CSV
5. **Webhooks**: Receber notificações de eventos externos
6. **Tratamento de Erros**: Validação e mensagens de erro claras

### Exercícios Práticos
Ver **[GUIA_MERCADO_PAGO.md](GUIA_MERCADO_PAGO.md)** para exercícios passo a passo.

## ⚙️ Automação

O sistema utiliza Python para automatizar:
1. **Leitura de dados** das obras (CSV)
2. **Geração de links** de pagamento no Mercado Pago
3. **Criação de QR Codes** para cada obra
4. **Geração de páginas HTML** individuais
5. **Processamento de pagamentos** via webhook

## 🔧 Uso Avançado

### Gerar Links para Todas as Obras
```python
from mercado_pago_api import generate_all_payment_links

df = generate_all_payment_links('obras_com_links.csv')
print(df)
```

### Criar Link para Obra Específica
```python
from mercado_pago_api import MercadoPagoConfig, ObrasManager, MercadoPagoPayment

config = MercadoPagoConfig()
obras = ObrasManager()
mp = MercadoPagoPayment(config, obras)

resultado = mp.create_payment_preference(item_number=1, max_installments=6)
print(resultado['payment_link'])
```

## 🧪 Testando Pagamentos

Use cartões de teste do Mercado Pago:

**Cartão Aprovado:**
- Número: `5031 4332 1540 6351`
- CVV: `123`
- Vencimento: qualquer data futura

**Mais cartões:** https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/additional-content/test-cards

## 🌐 Deploy

### GitHub Pages (Frontend)
O site estático já está hospedado no GitHub Pages.

### Backend (Webhook)
Para produção, você precisa hospedar o `webhook_mercadopago.py`:
- Heroku (gratuito)
- PythonAnywhere
- AWS Lambda
- Google Cloud Functions

## 🔒 Segurança

- ✅ Credenciais em arquivo `.env` (não commitado)
- ✅ `.gitignore` protege informações sensíveis
- ✅ Token de teste para desenvolvimento
- ✅ Validação de dados antes de enviar ao MP

## 📊 Dados das Obras

O arquivo `dados_obras.csv` contém:
- ITEM (número da obra)
- TELAS (nome)
- TÉCNICA
- DIMENSÃO
- ANO
- VALOR (R$)
- VALOR_PIX (com desconto)
- PARCELAMENTO
- CATEGORIA

## 🤝 Contribuindo

Contribuições são bem-vindas! Este é um projeto educacional.

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

## 👨‍💻 Autor

**Pedro Canuto**
- GitHub: [@DataCanuto](https://github.com/DataCanuto)
- LinkedIn: [Pedro Canuto](https://linkedin.com/in/pedrocanuto)

**Artista:**
Paulo Canuto - Artista Plástico

## 🙏 Agradecimentos

- Mercado Pago pela API e documentação
- Comunidade Python
- GitHub Pages por hospedar o frontend

---

## 📞 Suporte

Se tiver dúvidas sobre a integração do Mercado Pago:
1. Consulte o [GUIA_MERCADO_PAGO.md](GUIA_MERCADO_PAGO.md)
2. Veja exemplos no código comentado
3. Abra uma issue no GitHub

---

**⭐ Se este projeto te ajudou, deixe uma estrela!**
