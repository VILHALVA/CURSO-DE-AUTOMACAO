from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicialize o driver do Chrome (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

# Abra o Google
driver.get("https://www.google.com")

# Encontre o campo de pesquisa pelo nome "q" e insira uma consulta
search_box = driver.find_element_by_name("q")
search_box.send_keys("Automação web com Python e Selenium")
search_box.send_keys(Keys.RETURN)

# Aguarde alguns segundos para os resultados serem exibidos
import time
time.sleep(5)

# Imprima os resultados
search_results = driver.find_elements_by_css_selector(".g")
for result in search_results:
    print(result.text)

# Feche o navegador
driver.close()
