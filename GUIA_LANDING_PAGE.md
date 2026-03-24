# Sistema de Landing Page Dinâmica - Paulo Canuto

## 📋 Descrição

Uma aplicação web responsiva e modular que transforma o catálogo de obras em uma landing page profissional e mostruário para o artista Paulo Canuto. O sistema é totalmente dinâmico e sua atualiza automaticamente conforme mudanças nos dados.

## 🏗️ Arquitetura

### 1. **Landing Page Principal** (`index.html`)
- Hero section com biografia do artista
- Seção "Sobre o Artista" com highlights
- Galeria de categorias com cards interativos
- Seção de textos curatoriais
- Sistema de comentários (localStorage)
- Header sticky com navegação responsiva
- Footer com informações de contato

### 2. **Banco de Dados** (`assets/data/obras.json`)
- Dados centralizados em formato JSON
- Estrutura clara e fácil de manter
- Informações do artista
- Lista de categorias
- Lista completa de obras
- Textos curatoriais

### 3. **Galeria Dinâmica** (`pages/galeria.html`)
- Página específica por categoria
- Filtros por status (Disponível, Vendido, Todas)
- Cards de obras com informações
- Links diretos para WhatsApp
- Responsiva para mobile

### 4. **Script de Atualização** (`atualizar_dados.py`)
- Extrai informações dos arquivos HTML das obras
- Popula automaticamente o JSON
- Detecta categoria pelo título
- Atualiza status de disponibilidade
- Extrai preços e dados técnicos

### 5. **Sistema de Comentários** (localStorage)
- Comentários armazenados localmente
- Sem necessidade de servidor
- Persistência entre sessões

## 🚀 Como Usar

### Primeira Configuração

```bash
# 1. Instalar dependências Python
pip install beautifulsoup4

# 2. Executar script para popular JSON
python atualizar_dados.py

# 3. Abrir index.html em um navegador
# (ou usar um servidor local, ex: python -m http.server)
```

### Adicionar/Atualizar Obras

1. **Método Automático (Recomendado):**
   - Atualizar os arquivos HTML em `links_obras/item_X/index.html`
   - Executar: `python atualizar_dados.py`
   - O JSON será atualizado automaticamente

2. **Método Manual:**
   - Editar diretamente `assets/data/obras.json`
   - Adicionar/modificar campo de status, preço, disponibilidade

### Mudar Status de uma Obra

No arquivo `assets/data/obras.json`, localize a obra e altere:
```json
"status": "disponivel"  // ou "vendido"
```

A landing page refletirá a mudança automaticamente.

## 📱 Responsividade

O site é totalmente responsivo:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

Menu mobile com toggle está implementado.

## 🎯 Funcionalidades Principais

### ✨ Landing Page
- [x] Hero section sofisticado
- [x] Biografia do artista
- [x] Categorias de obras
- [x] Galeria destacada (6 primeiras obras)
- [x] Textos curatoriais
- [x] Sistema de comentários
- [x] CTA buttons para contato via WhatsApp

### 🖼️ Galeriacategoria
- [x] Filtros por status
- [x] Grid responsivo
- [x] Links para WhatsApp
- [x] Informações técnicas
- [x] Preços dinâmicos

### 📊 Dados Dinâmicos
- [x] JSON centralizado
- [x] Script Python para atualização automática
- [x] Categorias com contagem automática
- [x] Status de disponibilidade

### 💬 Comentários
- [x] Formulário simples
- [x] Armazenamento em localStorage
- [x] Lista de comentários em tempo real
- [x] Validação básica

## 📁 Estrutura de Pastas

```
galeria-digital-artes/
├── index.html                          # Landing page principal
├── atualizar_dados.py                  # Script de atualização
├── assets/
│   ├── data/
│   │   └── obras.json                  # Banco de dados
│   ├── css/
│   │   └── style.css                   # Estilos
│   └── img/
│       └── [imagens das obras]
├── pages/
│   └── galeria.html                    # Página de galeria por categoria
├── links_obras/
│   ├── item_1/
│   │   └── index.html
│   ├── item_2/
│   │   └── index.html
│   └── [outras obras]
└── catalog_mobile/
    └── index.html                      # Catálogo original (mantido)
```

## 🔄 Fluxo de Atualização

```
Modificar HTML das obras
    ↓
Executar atualizar_dados.py
    ↓
JSON é atualizado automaticamente
    ↓
Landing page reflete mudanças
    ↓
Galeria dinâmica mostra status correto
```

## 🎨 Customização

### Cores
Editar `:root` em `index.html`:
```css
--primary-color: #1a1a1a;
--accent-color: #d4af37;
```

### Textos Curatoriais
Editar `assets/data/obras.json` > `textos_curatoriais`

### Informações do Artista
Editar `assets/data/obras.json` > `artista`

## 🔧 Manutenção

### Executar Atualização Mensal
```bash
# Atualizar JSON com dados mais recentes
python atualizar_dados.py
```

### Backup de Dados
```bash
# Fazer backup do JSON
cp assets/data/obras.json assets/data/obras_backup.json
```

## 📞 Contato

- WhatsApp: +55 71 99958-8950
- Email: contato@paulocanuto.com
- Instagram: @paulocanuto

## 📝 Versions

- **v1.0** - Lançamento inicial
  - Landing page
  - Galeria dinâmica
  - Sistema de comentários
  - Script de atualização

## 🤝 Contribuições

Este projeto foi desenvolvido especificamente para presentar o trabalho de Paulo Canuto. Sugestões e melhorias são bem-vindas!

---

**Desenvolvido com dedicação ao arte de Paulo Canuto**
