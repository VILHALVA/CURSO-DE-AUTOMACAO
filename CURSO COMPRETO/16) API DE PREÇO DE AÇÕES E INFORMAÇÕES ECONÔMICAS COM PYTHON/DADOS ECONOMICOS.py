import requests

# Insira sua chave de API do Quandl aqui
api_key = 'SUA_CHAVE_DE_API'

# Código de acesso para um conjunto de dados específico (por exemplo, 'FRED/GDP' para o PIB dos EUA)
dataset_code = 'FRED/GDP'

# Faça uma solicitação para obter os dados econômicos
url = f'https://www.quandl.com/api/v3/datatables/{dataset_code}.json?api_key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ao acessar a API do Quandl.')
