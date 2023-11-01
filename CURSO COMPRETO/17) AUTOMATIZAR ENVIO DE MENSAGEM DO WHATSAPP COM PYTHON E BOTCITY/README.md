# AUTOMATIZAR ENVIO DE MENSAGEM DO WHATSAPP COM PYTHON E BOTCITY
É possível automatizar o envio de mensagens do WhatsApp com Python e Botcity. Para isso, você precisará seguir estas etapas:

1. **Crie uma conta no Botcity.** Você pode fazer isso indo ao site do Botcity e clicando no botão "Registrar".
2. **Crie um workspace.** Um workspace é um espaço de trabalho no Botcity onde você pode criar e gerenciar seus robôs.
3. **Crie um robô.** Para criar um robô, você precisará fornecer um nome para o robô, uma descrição e uma linguagem de programação.
4. **Crie um script para o robô.** O script é o código que o robô usará para executar a tarefa.
5. **Teste o robô.** Uma vez que você tenha criado um script para o robô, você precisará testá-lo para garantir que ele funcione corretamente.
6. **Implemente o robô.** Depois de testar o robô, você poderá implementá-lo para que ele comece a automatizar a tarefa.

**Exemplo de script:**

Aqui está um exemplo de script Python que envia uma mensagem do WhatsApp:

```python
from botcity import Browser

def send_message(number, message):
    # Crie um robô
    robot = Browser()

    # Abra o WhatsApp Web
    robot.open("https://web.whatsapp.com")

    # Acesse a conversa do destinatário
    input_number = robot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/input")
    input_number.send_keys(number)
    input_number.send_keys(u"\ue007")

    # Digite a mensagem
    input_message = robot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/input")
    input_message.send_keys(message)

    # Envie a mensagem
    pyautogui.press("enter")

# Envia uma mensagem para o número 1234567890
send_message("1234567890", "Olá, como vai?")
```

Este script irá primeiro abrir o WhatsApp Web no navegador da web. Em seguida, ele irá acessar a conversa do destinatário digitando o número no campo de pesquisa. Depois disso, ele irá digitar a mensagem no campo de mensagem. Finalmente, ele irá enviar a mensagem pressionando a tecla enter.

**Observações:**

* Para que este script funcione, você precisará ter o Chrome instalado em seu computador.
* Você também precisará ter uma conta do WhatsApp e saber o número de telefone do destinatário.

**Avançado:**

Você pode usar este script como base para criar automações mais complexas, como:

* Enviar mensagens em massa.
* Enviar mensagens personalizadas.
* Enviar mensagens com anexos.

**Considerações finais:**

É importante usar esse recurso com responsabilidade e evitar enviar mensagens indesejadas ou spam.