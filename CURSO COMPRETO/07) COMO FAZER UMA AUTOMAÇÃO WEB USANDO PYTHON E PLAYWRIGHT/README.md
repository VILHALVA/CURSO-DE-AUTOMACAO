# COMO FAZER UMA AUTOMAÇÃO WEB USANDO PYTHON E PLAYWRIGHT?
O Playwright é uma biblioteca que permite automatizar interações em navegadores da web, e é uma alternativa ao Selenium. Ele oferece suporte a múltiplos navegadores, incluindo Chromium, Firefox e WebKit, e fornece uma API amigável para automatizar ações em páginas da web. Abaixo estão os passos para criar uma automação web simples usando Python e Playwright:

**Passo 1: Instalar o Playwright e configurar o ambiente**

Antes de começar, certifique-se de ter o Python instalado em seu sistema. Em seguida, você pode instalar o Playwright e os navegadores que deseja usar (por exemplo, Chromium) usando o seguinte comando:

```bash
pip install playwright
playwright install
```

**Passo 2: Escrever o código de automação web**

Aqui está um exemplo simples de um script Python usando o Playwright para abrir uma página da web, preencher um campo de texto, clicar em um botão e capturar um screenshot da página:

```python
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://exemplo.com")  # Substitua com o URL do site que deseja automatizar

        # Preencher um campo de texto
        page.fill("input[name='username']", "seu_usuario")

        # Clicar em um botão
        page.click("button[type='submit']")

        # Capturar um screenshot da página
        page.screenshot(path="screenshot.png")

        browser.close()

if __name__ == "__main__":
    main()
```

Certifique-se de substituir a URL, o seletor CSS para o campo de texto e o seletor CSS para o botão com os valores apropriados para o site que deseja automatizar.

**Passo 3: Execute o script**

Salve o código em um arquivo Python (por exemplo, `automacao_playwright.py`) e execute-o com o Python. Isso abrirá o navegador, automatizará as ações especificadas e capturará um screenshot da página.

Este é apenas um exemplo simples de automação web com Playwright. A biblioteca oferece muitos recursos avançados, como interações com elementos de página, preenchimento de formulários, manipulação de cookies, navegação entre páginas e muito mais. Consulte a documentação do Playwright para obter informações detalhadas: [Documentação do Playwright](https://playwright.dev/docs/intro).

Lembre-se de que, ao criar automações web, é importante respeitar os termos de uso do site que você está automatizando e garantir que sua automação seja ética e legal.