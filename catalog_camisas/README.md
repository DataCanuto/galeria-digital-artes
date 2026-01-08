# Catálogo de Camisas - Paulo Canuto

## Descrição

Este diretório contém o catálogo digital exclusivo de camisas com obras de Paulo Canuto. O catálogo foi gerado automaticamente a partir dos dados estruturados em `db_camisas.csv` e apresenta todas as 188 peças organizadas por tema (alfabético) com detalhes como cor, tamanho, descrição e imagens de alta qualidade.

## Estrutura de Arquivos

```
catalog_camisas/
├── index.html                    # Página principal do catálogo
├── db_camisas.csv               # Base de dados com informações das camisas
├── gerar_catalogo_camisas.py    # Script Python de geração
├── FotosCamisas/                # Diretório com todas as imagens das camisas
│   ├── IMG_2654.JPEG
│   ├── IMG_2655.JPEG
│   └── ... (52 imagens)
└── README.md                    # Este arquivo
```

## Dados e Campos

O arquivo `db_camisas.csv` contém os seguintes campos para cada camisa:

- **item**: Número sequencial (1-188)
- **cor**: Cor da camisa (branca, preta, creme, mostarda, azul, grafite, terracota, preta, etc.)
- **tema**: Categoria/tema da camisa (Bicicletas, Carros, Indígena, Moto, Plantas, Portas e Janelas)
- **tela**: Número de variação do tema
- **tamanho**: Tamanho disponível (P, M, G, XG, GG, EXG, etc.)
- **Titulo/Descrição**: Descrição detalhada da obra
- **Ano**: Ano de criação
- **REFERÊNCIA**: Identificador único para localizar a imagem no diretório FotosCamisas

## Geração do Catálogo

### Método

O catálogo foi gerado automaticamente usando o script Python `gerar_catalogo_camisas.py` que:

1. **Lê o arquivo CSV** com todos os dados das camisas
2. **Agrupa as camisas por tema** em ordem alfabética
3. **Ordena alfabeticamente os temas**:
   - Bicicletas (10 peças)
   - Carros (10 peças)
   - Indígena (12 peças)
   - Moto (1 peça)
   - Plantas (12 peças)
   - Portas e Janelas (8 peças)
4. **Localiza automaticamente as imagens** usando o campo REFERÊNCIA
5. **Gera o HTML responsivo** com formatação profissional

### Execução

```bash
cd catalog_camisas
python gerar_catalogo_camisas.py
```

## Características do HTML Gerado

- ✅ **Responsivo**: Funciona perfeitamente em mobile, tablet e desktop
- ✅ **Design Consistente**: Mantém o padrão visual do catálogo_mobile
- ✅ **Fundo Escuro**: Tema dark (#1a1a1a) com textos em branco
- ✅ **Imagens Otimizadas**: Lazy loading para melhor performance
- ✅ **Agrupamento por Tema**: Camisas organizadas com subheaders visuais
- ✅ **Botão de Retorno**: Link para voltar ao catálogo_mobile
- ✅ **Animações Suaves**: Transições elegantes ao interagir com elementos

## Navegação

### Do Catálogo Mobile Para Camisas

1. **Menu Horizontal**: Um novo botão "CATÁLOGO DE CAMISAS" foi adicionado ao menu suspenso do catálogo_mobile
2. **Seção Camisas**: A seção de camisas no catálogo_mobile agora apresenta um botão destacado "ACESSAR CATÁLOGO COMPLETO DE CAMISAS"

### Do Catálogo de Camisas Para Catálogo Mobile

- Um botão "VOLTAR AO CATÁLOGO" aparece no header do catálogo de camisas
- Um botão de retorno aparece ao final do catálogo de camisas

## Campos Exibidos em Cada Peça

Para cada camisa são exibidos:

```
Nome: [TEMA] [NÚMERO]
Tamanho: [TAMANHO]
Cor: [COR] | [DESCRIÇÃO]
```

**Exemplo:**
```
Nome: Bicicletas 1
Tamanho: G
Cor: branca | Mercedes Damenrad
```

## Principais Temas Representados

| Tema | Quantidade | Descrição |
|------|-----------|-----------|
| **Bicicletas** | 10 | Diversos modelos de bicicletas e ciclistas |
| **Carros** | 10 | Automóveis clássicos e modernos |
| **Indígena** | 12 | Arte indígena e elementos culturais |
| **Moto** | 1 | Motocicletas (Lambretta) |
| **Plantas** | 12 | Flora, flores e elementos naturais |
| **Portas e Janelas** | 8 | Arquitetura urbana e fachadas |

## Performance e Otimização

- **Lazy Loading**: Imagens carregam conforme o usuário desce a página
- **Minificação de CSS**: Todos os estilos estão inlined para menos requisições
- **Cache de Imagens**: Suporta navegador cache para retorno rápido
- **Responsive Design**: Adapta-se automaticamente a qualquer tamanho de tela

## Manutenção

### Para Adicionar Novas Camisas

1. Adicione uma linha no `db_camisas.csv` com os dados completos
2. Salve a imagem em `FotosCamisas/` com o nome `IMG_XXXX.JPEG`
3. Execute novamente:
   ```bash
   python gerar_catalogo_camisas.py
   ```

### Para Modificar Cores ou Agrupamento

1. Edite o arquivo `db_camisas.csv` conforme necessário
2. Execute novamente o script para regenerar o HTML

## Compatibilidade

- ✅ Chrome/Edge (versões recentes)
- ✅ Firefox (versões recentes)
- ✅ Safari (iOS 12+)
- ✅ Navegadores mobile modernos

## Notas de Design

- Mantém a paleta de cores do artista (fundo escuro, vermelho #e53935 para destaques)
- Tipografia Georgia para elegância e corpora de imagem
- Espaçamento generoso para melhor legibilidade
- Animações suaves para transições agradáveis

---

**Última atualização**: 8 de janeiro de 2026
**Total de peças**: 188 camisas
**Temas**: 6 categorias
