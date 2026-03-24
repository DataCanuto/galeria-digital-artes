# 🎨 Landing Page Paulo Canuto - Sistema Completo

Uma solução profissional, responsiva e dinâmica para transformar o portfólio artístico de Paulo Canuto em uma presença web moderna.

## 📌 O Que Foi Desenvolvido

### 1. **Landing Page Sofisticada** 
- Hero section elegante com biografia do artista
- Seções bem estruturadas sobre as técnicas e obras
- Design moderno com paleta de cores profissional
- Totalmente responsivo (mobile, tablet, desktop)

### 2. **Sistema de Dados Dinâmico**
- Banco de dados centralizado em JSON
- Script Python para atualizar automaticamente
- Mudanças refletem em tempo real na página
- Sistema de status de disponibilidade (Disponível/Vendido)

### 3. **Galeria Inteligente**
- Filtros por status e categoria
- Cards interativas com informações técnicas
- Preços formatados automaticamente
- Links diretos para WhatsApp

### 4. **Sistema de Comentários**
- Sem necessidade de servidor
- Armazenamento em localStorage (browser)
- Moderação simples
- Persiste entre sessões

### 5. **Textos Curatoriais Integrados**
- "Minhas palavras sobre a mostra" - Paulo Canuto
- "Um artista, a cidade, seus ocupantes e seus meios" - Chico Mazzoni
- "Paulo Canuto: A Cidade em Movimento" - Marcos Rodrigues

## 🚀 Início Rápido

### Opção 1: Instalação Automatizada (Recomendado)

```bash
# Windows
python setup.py

# Linux/Mac
python3 setup.py
```

### Opção 2: Instalação Manual

1. **Instalar Python 3.7+** (se não tiver)
   - Download em: https://www.python.org/

2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Atualizar dados**
   ```bash
   python atualizar_dados.py
   ```

4. **Servir localmente**
   ```bash
   python -m http.server 8000
   ```

5. **Acessar**
   - Abra: http://localhost:8000

## 📂 Estrutura do Projeto

```
📦 galeria-digital-artes/
│
├── 📄 index.html                  ← LANDING PAGE PRINCIPAL
├── 📄 setup.py                    ← Script de inicialização
├── 📄 atualizar_dados.py          ← Atualiza JSON automaticamente
├── 📄 config.json                 ← Configurações da aplicação
│
├── 📁 pages/
│   └── galeria.html               ← Página de galeria por categoria
│
├── 📁 assets/
│   ├── data/
│   │   └── obras.json             ← 📊 BANCO DE DADOS
│   ├── css/
│   │   └── style.css              ← Estilos compartilhados
│   └── img/
│       └── [imagens das obras]
│
├── 📁 links_obras/
│   ├── item_1/index.html
│   ├── item_2/index.html
│   └── ... item_58/index.html
│
└── 📁 catalog_mobile/
    └── index.html                 ← Catálogo original (mantido)
```

## 💡 Como Usar

### Visualizar a Landing Page
1. Abra `index.html` diretamente no navegador, ou
2. Use um servidor local: `python -m http.server 8000`

### Explorar Categorias
- Clique em qualquer categoria na landing page
- Será redirecionado para `pages/galeria.html?category=telas` (exemplo)
- Use os filtros para filtrar por status

### Fazer um Comentário
- Role até a seção "Comentários & Feedback"
- Preencha nome, email e mensagem
- Clique "Enviar Comentário"
- Seu comentário aparecerá na lista em tempo real

### Expressar Interesse em uma Obra
- Clique em "Expressar Interesse" ou "Fale com o Monitor"
- Será aberto o WhatsApp com mensagem pré-preenchida
- Siga a conversa com o monitor de vendas

## 🔄 Quando uma Obra é VENDIDA

**Processo de atualização:**

1. **Opção 1: Automática**
   - Editar o arquivo HTML da obra em `links_obras/item_X/index.html`
   - Remover ou comentar o `whatsapp-button`
   - Executar: `python atualizar_dados.py`
   - Status muda para "VENDIDO" automaticamente

2. **Opção 2: Manual**
   - Abrir `assets/data/obras.json`
   - Localizar a obra
   - Trocar: `"status": "disponivel"` por `"status": "vendido"`
   - Salvar arquivo

3. **Resultado**
   - Landing page mostra "VENDIDO"
   - Galeria dinâmica mostra "VENDIDO"
   - Botão de contato pode ser desabilitado

## 🎨 Personalização

### Mudar as Cores
Editar as variáveis CSS em `index.html` (linhas ~48-56):
```css
:root {
    --primary-color: #1a1a1a;      /* Preto */
    --accent-color: #d4af37;       /* Ouro */
    --light-bg: #f5f5f5;            /* Cinza claro */
}
```

### Adicionar Redes Sociais
Editar `assets/data/obras.json`:
```json
"redes_sociais": {
    "instagram": "seu-perfil",
    "facebook": "seu-perfil",
    "tiktok": "seu-perfil"
}
```

### Modificar Textos Curatoriais
Editar `assets/data/obras.json` > `textos_curatoriais`

## 📱 Responsividade

A aplicação é 100% responsiva:

- ✅ **Desktop** (1200px+)
  - Grid de 3 colunas
  - Layout completo com sidebars

- ✅ **Tablet** (768px - 1199px)
  - Grid de 2 colunas
  - Menu adaptado

- ✅ **Mobile** (<768px)
  - Grid de 1 coluna
  - Menu hamburger
  - Toque otimizado

## 🔐 Segurança & Privacidade

- ✅ Nenhum dado é armazenado em servidor
- ✅ Comentários ficam apenas no navegador (localStorage)
- ✅ WhatsApp é gerenciado pelo próprio usuário
- ✅ Sem rastreamento de terceiros
- ✅ HTTPS recomendado para produção

## 📊 Analytics (Opcional)

Para adicionar analytics, insira o código no `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

## 🚀 Deploy (Hospedagem)

### GitHub Pages (Grátis)
1. Criar repositório `paulocanuto.github.io`
2. Push do código para GitHub
3. Site disponível em: `https://paulocanuto.github.io`

### Vercel (Grátis)
1. Conectar repositório GitHub
2. Deploy automático
3. Domínio personalizado disponível

### Servidor Próprio
1. Upload dos arquivos via FTP
2. Não requer servidor especial (HTML + JSON + Python)
3. Executar `python atualizar_dados.py` periodicamente

## 📞 Suporte & Contato

- **WhatsApp:** +55 71 99958-8950
- **Email:** contato@paulocanuto.com
- **Instagram:** @paulocanuto

## 📝 Tarefas de Manutenção

### Mensal
- [ ] Executar `python atualizar_dados.py`
- [ ] Fazer backup do `assets/data/obras.json`

### Trimestral
- [ ] Revisar comentários
- [ ] Atualizar preços se necessário

### Anual
- [ ] Revisar e atualizar textos curatoriais
- [ ] Adicionar novas obras
- [ ] Avaliar feedback de visitantes

## 🎯 Próximos Passos Sugeridos

1. ✅ Testar a landing page em diferentes dispositivos
2. ✅ Customizar cores e fonts
3. ✅ Atualizar todas as obras no banco de dados
4. ✅ Testar sistema de comentários
5. ✅ Configurar domínio personalizado
6. ✅ Ativar HTTPS
7. ✅ Adicionar analytics
8. ✅ Otimizar imagens das obras

## 📚 Documentação Completa

Para documentação mais detalhada, leia:
- **GUIA_LANDING_PAGE.md** - Guia técnico completo
- **config.json** - Configurações da aplicação
- **atualizar_dados.py** - Documentação do script

## 🎉 Conclusão

Você agora tem uma landing page profissional, responsiva e totalmente dinâmica para apresentar o trabalho de Paulo Canuto ao mundo!

Qualquer dúvida ou sugestão, entre em contato via WhatsApp ou email.

---

**Desenvolvido com dedicação ao trabalho artístico de Paulo Canuto**

**Versão:** 1.0.0  
**Data:** Março de 2025  
**Status:** ✅ Pronto para produção
