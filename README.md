# galeria-digital-pcanuto
Repositório de arquivos.html acesso via qr code em exposição de artes, Salvador-Bahia. 

# 🎨 Galeria Digital & QR Code System - Paulo Canuto

Este projeto consiste em uma solução de **Galeria Digital Interativa** desenvolvida para a exposição do artista plástico **Paulo Canuto**. O sistema conecta obras físicas ao ambiente digital através de QR Codes, permitindo a compra direta e contato com o artista.

Embora o resultado final seja uma interface Front-End hospedada no GitHub Pages, o projeto conta com uma pipeline de automação em **Python** para gerenciamento de dados e construção das páginas.

## 🚀 Funcionalidades

* **Catalogação Digital:** Páginas individuais para cada obra de arte com design responsivo e catálogo completo.
* **Integração Comercial:** Botões de compra integrados diretamente com links de pagamento do **Mercado Pago**.
* **Contato Direto:** Integração via API de link do **WhatsApp** para negociação direta com o artista.
* **Acesso via QR Code:** Otimização para acesso mobile rápido durante a visita à exposição.

## 🛠 Tecnologias Utilizadas

Este projeto utiliza uma abordagem híbrida, usando Python para "pré-processar" o site estático:

* **Python:** Utilizado para a lógica de automação (Scripting).
    * Leitura de dados das obras (CSV/Estruturas de dados).
    * Geração automatizada dos arquivos HTML (evitando repetição de código manual).
    * Automação da criação de pastas e organização dos assets.
* **HTML5 & CSS3:**
    * Estruturação semântica.
    * Estilização responsiva (Mobile First).
    * Design limpo focado na apreciação das obras.
* **Git & GitHub Pages:** Versionamento e hospedagem gratuita e escalável.

## ⚙️ Como funciona a Automação

Diferente de um site estático comum feito página por página, desenvolvi um script em Python que atua como um *Static Site Generator* simples:
1.  O script lê as informações das obras (Título, Preço, Dimensões, Links de Pagamento).
2.  Insere esses dados em um template HTML padrão.
3.  Gera os arquivos finais prontos para o deploy no GitHub Pages.

## author

Desenvolvido por Pedro Canuto.
