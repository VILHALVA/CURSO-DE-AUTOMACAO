# COMO LER ARQUIVO EM EXCEL COM VÁRIAS ABAS NO PYTHON [PANDAS]
Para ler um arquivo Excel com várias abas usando a biblioteca Pandas em Python, você pode usar a função `read_excel` do Pandas com a opção `sheet_name` para especificar qual aba deseja ler. Aqui está um exemplo de como ler um arquivo Excel com várias abas:

```python
import pandas as pd

# Substitua 'seuarquivo.xlsx' pelo caminho do seu arquivo Excel
file_path = 'seuarquivo.xlsx'

# Especifique o nome da aba que deseja ler ou use o índice da aba (0 para a primeira aba)
sheet_name = 'Nome da Aba'  # ou 0 para a primeira aba

# Use a função read_excel para ler a aba desejada em um DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Agora você pode trabalhar com o DataFrame 'df' que contém os dados da aba especificada
```

Neste exemplo, você deve substituir `'seuarquivo.xlsx'` pelo caminho do seu arquivo Excel e `'Nome da Aba'` pelo nome da aba que deseja ler. Se você deseja ler a primeira aba, pode usar o índice `0` em vez do nome da aba.

Lembre-se de que, se o arquivo Excel tiver várias abas que você deseja ler, você pode repetir o processo para cada aba ou usar um loop para automatizar a leitura de todas as abas, armazenando cada uma delas em um dicionário de DataFrames ou em uma lista. Por exemplo:

```python
# Lista de nomes das abas que deseja ler
aba_names = ['Aba1', 'Aba2', 'Aba3']

# Dicionário para armazenar os DataFrames de cada aba
aba_data = {}

for aba_name in aba_names:
    df = pd.read_excel(file_path, sheet_name=aba_name)
    aba_data[aba_name] = df
```

Desta forma, você terá um dicionário chamado `aba_data` contendo os DataFrames correspondentes a cada aba do arquivo Excel. Isso permite que você acesse facilmente os dados de cada aba individualmente.