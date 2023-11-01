# COMO CONVERTER EXTENSÃO DE IMAGENS COM PYTHON EM 5 LINHAS DE CÓDIGO?
Você pode converter a extensão de imagens em Python usando a biblioteca `Pillow`, que é uma extensão do módulo `PIL` (Python Imaging Library). Aqui está um exemplo de como fazer isso em cinco linhas de código:

**Passo 1: Instale a biblioteca Pillow:**

Se você ainda não a tiver instalado, pode fazê-lo usando o seguinte comando:

```bash
pip install Pillow
```

**Passo 2: Escreva o Código Python para Converter Extensões:**

```python
from PIL import Image

# Abrir a imagem de origem
imagem_origem = Image.open('imagem_origem.jpg')

# Salvar a imagem com a nova extensão (por exemplo, PNG)
imagem_origem.save('imagem_destino.png')
```

Neste exemplo, `imagem_origem.jpg` é a imagem de origem com a extensão JPG, e estamos convertendo-a para a extensão PNG ao salvar como `imagem_destino.png`. Você pode substituir as extensões e nomes dos arquivos de acordo com suas necessidades.

Essas cinco linhas de código abrem a imagem de origem, a convertem para o formato desejado e a salvam com a nova extensão. Certifique-se de ajustar os caminhos e nomes dos arquivos conforme necessário. A biblioteca Pillow oferece suporte a vários formatos de imagem comuns, como JPG, PNG, GIF, BMP, entre outros.