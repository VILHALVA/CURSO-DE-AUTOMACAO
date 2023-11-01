from PIL import Image

# Abrir a imagem de origem
imagem_origem = Image.open('imagem_origem.jpg')

# Salvar a imagem com a nova extensão (por exemplo, PNG)
imagem_origem.save('imagem_destino.png')
