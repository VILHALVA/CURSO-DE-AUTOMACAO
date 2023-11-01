# COMO CRIAR UMA AUTOMAÇÃO DE INSTAGRAM COM PYTHON?
Para criar uma automação de Instagram com Python, você precisará seguir estas etapas:

1. **Instalar as bibliotecas necessárias:** Você precisará instalar as seguintes bibliotecas Python:
    * **selenium:** Para controlar o navegador da web.
    * **requests:** Para fazer solicitações HTTP.

2. **Criar um script:** Você precisará criar um script Python que siga estas etapas:
    * **Abra o navegador da web.**
    * **Faça login no Instagram.**
    * **Execute as tarefas de automação.**

3. **Executar o script:** Você pode executar o script Python usando o seguinte comando:

```python
python script.py
```

**Exemplo de script**

Aqui está um exemplo de script Python que automatiza o compartilhamento de uma postagem no Instagram:

```python
import selenium
import requests

def share_post(url):
    # Abra o navegador da web
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.instagram.com")

    # Faça login no Instagram
    input_username = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/form/div/input[1]")
    input_username.send_keys("seu_usuário")
    input_password = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/form/div/input[2]")
    input_password.send_keys("sua_senha")
    button_login = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/form/div/div[3]/button")
    button_login.click()

    # Abra a postagem
    link = requests.get(url).text
    post_id = link.split("/")[-1]
    url_post = f"https://www.instagram.com/p/{post_id}"
    driver.get(url_post)

    # Compartilhe a postagem
    button_share = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/button")
    button_share.click()

# Compartilhe uma postagem
share_post("https://www.instagram.com/p/Cd8x72Xp42f/")
```

Este script irá primeiro abrir o navegador da web e fazer login no Instagram. Em seguida, ele irá abrir a postagem especificada pela URL. Finalmente, ele irá compartilhar a postagem clicando no botão "Compartilhar".

**Observações:**

* Para que este script funcione, você precisará ter o Chrome instalado em seu computador.
* Você também precisará ter uma conta do Instagram e saber as credenciais de login.

**Avançado:**

Você pode usar este script como base para criar automações mais complexas, como:

* Seguimento de usuários.
* Curtida de postagens.
* Comentário de postagens.
* Publicação de postagens.

É importante seguir as diretrizes do Instagram ao criar automações. O Instagram pode punir contas que violam essas diretrizes.