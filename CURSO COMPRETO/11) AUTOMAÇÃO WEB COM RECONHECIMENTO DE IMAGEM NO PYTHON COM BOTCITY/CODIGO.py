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
