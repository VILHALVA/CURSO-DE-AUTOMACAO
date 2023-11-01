import pandas as pd

# Especifique o caminho para o arquivo Excel
file_path = 'arquivo_excel.xlsx'

# Lista de nomes das abas que desejamos ler
aba_names = ['Aba1', 'Aba2', 'Aba3']

# Dicionário para armazenar os DataFrames de cada aba
aba_data = {}

# Loop para ler cada aba e armazenar em um dicionário
for aba_name in aba_names:
    df = pd.read_excel(file_path, sheet_name=aba_name)
    aba_data[aba_name] = df

# Exemplo de acesso aos dados em uma das abas (por exemplo, "Aba1")
df_aba1 = aba_data['Aba1']

# Agora você pode trabalhar com os DataFrames individuais, como df_aba1, df_aba2, etc.
