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
