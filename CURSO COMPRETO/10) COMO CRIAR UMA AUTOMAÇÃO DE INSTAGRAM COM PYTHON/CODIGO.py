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
