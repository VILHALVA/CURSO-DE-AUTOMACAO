# AUTOMAÇÃO WEB COM RECONHECIMENTO DE IMAGEM NO PYTHON COM BOTCITY
A automação web com reconhecimento de imagem no Python com BotCity é uma maneira poderosa de automatizar tarefas que exigem a interação com o navegador da web e o reconhecimento de imagens.

**Para automatizar uma tarefa com o BotCity, você precisará seguir estas etapas:**

1. **Crie uma conta no BotCity.** Você pode fazer isso indo ao site do BotCity e clicando no botão "Registrar".
<img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQX5UwsWPhU3u0m-TBOBx6gWS2Oy6oQeoTFc6V9rCVPcbMEB87qr5n_wbxX3Fv2" width="280"> <br>

2. **Crie um workspace.** Um workspace é um espaço de trabalho no BotCity onde você pode criar e gerenciar seus robôs.
<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQW6c2HhkBleZK8iRYVghHxHe7_MMZohkhaoKZ-YQOFhHlVHcnLiezKFmBU9znX" width="280"> <br>

3. **Crie um robô.** Para criar um robô, você precisará fornecer um nome para o robô, uma descrição e uma linguagem de programação.
2. **Crie um workspace.** Um workspace é um espaço de trabalho no BotCity onde você pode criar e gerenciar seus robôs.
<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQtsHp_joqRdtto07VFpRd0UIn38saB7wUo4-itePphA_IAIQ6C-hhAzND3zXPg" width="280"> <br>

4. **Crie um script para o robô.** O script é o código que o robô usará para executar a tarefa.
5. **Teste o robô.** Uma vez que você tenha criado um script para o robô, você precisará testá-lo para garantir que ele funcione corretamente.
6. **Implemente o robô.** Depois de testar o robô, você poderá implementá-lo para que ele comece a automatizar a tarefa.

**Exemplo de automação web com reconhecimento de imagem no Python com BotCity:**

Vamos supor que você deseja automatizar a tarefa de coletar o preço de um produto em um site de comércio eletrônico. Para fazer isso, você pode criar um robô no BotCity que siga estas etapas:

1. **Abra o site do comércio eletrônico no navegador da web.**
2. **Encontre o produto que deseja comprar.**
3. **Reconheça a imagem do produto.**
4. **Acesse a página do produto.**
5. **Colete o preço do produto.**

**Script para o robô:**

```python
import cv2
import numpy as np
from botcity import Browser

def get_product_price(image_path):
    # Carregue a imagem
    image = cv2.imread(image_path)

    # Converta a imagem para preto e branco
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecte os contornos da imagem
    contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontre o maior contorno
    max_contour = max(contours, key=cv2.contourArea)

    # Obtenha o ROI do contorno
    (x, y, w, h) = cv2.boundingRect(max_contour)
    roi = gray_image[y:y + h, x:x + w]

    # Reconheça o texto na imagem
    price = pytesseract.image_to_string(roi, lang="eng")

    return price

# Crie um robô
robot = Browser()

# Abra o site do comércio eletrônico
robot.open("https://www.amazon.com/")

# Encontre o produto que deseja comprar
product_image = robot.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a/img")
product_image.screenshot("product_image.png")

# Obtenha o preço do produto
product_price = get_product_price("product_image.png")

# Imprima o preço do produto
print(product_price)
```

Este script irá primeiro abrir o site do comércio eletrônico no navegador da web. Em seguida, ele irá encontrar o produto que deseja comprar usando o elemento de imagem. Depois disso, ele irá tirar uma captura de tela do produto e usá-la para reconhecer o preço. Finalmente, ele irá imprimir o preço do produto.

**Observações:**

* Para que este script funcione, você precisará ter o Chrome instalado em seu computador.
* Você também precisará ter uma conta no Amazon e saber o URL do produto que deseja comprar.

**Avançado:**

Você pode usar este script como base para criar automações mais complexas, como:

* Coleta de preços de vários.