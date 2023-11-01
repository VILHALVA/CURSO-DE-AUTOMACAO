from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

# Carregue o modelo do contrato
modelo_contrato = Document("modelo_contrato.docx")

# Dados do contrato (substitua com seus próprios dados)
nome_cliente = "Nome do Cliente"
data_contrato = "01 de janeiro de 2023"
valor_contrato = "R$ 10.000,00"

# Substitua os espaços reservados no modelo pelo conteúdo desejado
for paragrafo in modelo_contrato.paragraphs:
    if "NOME_DO_CLIENTE" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace("NOME_DO_CLIENTE", nome_cliente)
    if "DATA_DO_CONTRATO" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace("DATA_DO_CONTRATO", data_contrato)
    if "VALOR_DO_CONTRATO" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace("VALOR_DO_CONTRATO", valor_contrato)

# Salve o contrato final
modelo_contrato.save("contrato_final.docx")
