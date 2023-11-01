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
