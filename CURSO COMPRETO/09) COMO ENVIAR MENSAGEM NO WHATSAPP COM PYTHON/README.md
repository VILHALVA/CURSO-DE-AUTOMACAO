# COMO ENVIAR MENSAGEM NO WHATSAPP COM PYTHON?
Para enviar uma mensagem no WhatsApp com Python de forma automática e completa, você precisará seguir estas etapas:

1. **Instalar as bibliotecas necessárias:** Você precisará instalar as seguintes bibliotecas Python:
    * **selenium:** Para controlar o navegador da web.
    * **pyautogui:** Para controlar o mouse e o teclado.

2. **Criar um script:** Você precisará criar um script Python que siga estas etapas:
    * **Abra o WhatsApp Web no navegador.**
    * **Acesse a conversa do destinatário.**
    * **Digite a mensagem.**
    * **Envie a mensagem.**

3. **Executar o script:** Você pode executar o script Python usando o seguinte comando:

```python
python script.py
```

**Exemplo de script**

Aqui está um exemplo de script Python que envia uma mensagem no WhatsApp:

```python
import selenium
import pyautogui

def send_message(number, message):
    # Abra o WhatsApp Web no navegador
    driver = selenium.webdriver.Chrome()
    driver.get("https://web.whatsapp.com")

    # Acesse a conversa do destinatário
    input_number = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/input")
    input_number.send_keys(number)
    input_number.send_keys(u"\ue007")

    # Digite a mensagem
    input_message = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/input")
    input_message.send_keys(message)

    # Envie a mensagem
    pyautogui.press("enter")

# Envia uma mensagem para o número 1234567890
send_message("1234567890", "Olá, como vai?")
```

Este script irá primeiro abrir o WhatsApp Web no navegador. Em seguida, ele irá acessar a conversa do destinatário digitando o número no campo de pesquisa. Depois disso, ele irá digitar a mensagem no campo de mensagem. Finalmente, ele irá enviar a mensagem pressionando a tecla enter.

**Observações:**

* Para que este script funcione, você precisará ter o WhatsApp Web instalado em seu computador.
* Você também precisará ter a permissão do destinatário para enviar mensagens para ele.

**Avançado:**

Para enviar mensagens em massa no WhatsApp, você pode usar um loop para iterar sobre uma lista de números de telefone. Também é possível usar uma biblioteca de reconhecimento de imagem para extrair os números de telefone de uma imagem ou documento.