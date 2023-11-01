import pytesseract

def break_captcha(image_path):
    # Carregue a imagem
    image = cv2.imread(image_path)

    # Converta a imagem para preto e branco
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Redimensione a imagem
    gray_image = cv2.resize(gray_image, (200, 200))

    # Denoise a imagem
    gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Encontre os contornos da imagem
    contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontre o maior contorno
    max_contour = max(contours, key=cv2.contourArea)

    # Obtenha o ROI do contorno
    (x, y, w, h) = cv2.boundingRect(max_contour)
    roi = gray_image[y:y + h, x:x + w]

    # Reconheça o texto na imagem
    text = pytesseract.image_to_string(roi, lang="eng")

    return text

# Quebre o CAPTCHA
text = break_captcha("captcha.png")

# Imprima o texto
print(text)