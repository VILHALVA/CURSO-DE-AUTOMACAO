# INTEGRAÇÃO ENTRE PYTHON E POWERPOINT - CRIAR APRESENTAÇÃO AUTOMATICAMENTE
Você pode criar apresentações no Microsoft PowerPoint automaticamente a partir do Python usando a biblioteca `python-pptx`. Com essa biblioteca, você pode criar slides, adicionar texto, imagens, tabelas e outros elementos aos slides. Aqui está um exemplo simples de como criar uma apresentação automaticamente:

**Passo 1: Instalar a biblioteca `python-pptx`**

Se você ainda não a tiver instalado, pode fazê-lo com o seguinte comando:

```bash
pip install python-pptx
```

**Passo 2: Escrever o Código Python para Criar a Apresentação**

Aqui está um exemplo de código Python que cria uma apresentação simples com dois slides:

```python
from pptx import Presentation
from pptx.util import Inches

# Crie uma apresentação vazia
apresentacao = Presentation()

# Crie o primeiro slide
slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[0])
titulo1 = slide1.shapes.title
titulo1.text = "Título do Slide 1"
conteudo1 = slide1.shapes.add_textbox(Inches(1), Inches(2), Inches(4), Inches(2))
texto1 = conteudo1.text_frame
texto1.text = "Este é o conteúdo do Slide 1."

# Crie o segundo slide
slide2 = apresentacao.slides.add_slide(apresentacao.slide_layouts[1])
titulo2 = slide2.shapes.title
titulo2.text = "Título do Slide 2"
conteudo2 = slide2.shapes.add_textbox(Inches(1), Inches(2), Inches(4), Inches(2))
texto2 = conteudo2.text_frame
texto2.text = "Este é o conteúdo do Slide 2."

# Salve a apresentação em um arquivo
apresentacao.save("minha_apresentacao.pptx")
```

Neste exemplo, estamos criando uma apresentação com dois slides. Você pode personalizar o título, o conteúdo e a aparência dos slides conforme necessário. Lembre-se de que a biblioteca `python-pptx` oferece muitos recursos para criar apresentações mais complexas, como adicionar imagens, tabelas, gráficos e formatação avançada.

Após criar a apresentação, você pode salvá-la em um arquivo usando o método `apresentacao.save()`. Certifique-se de ajustar os caminhos e os nomes de arquivo conforme necessário.