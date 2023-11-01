import requests

# Insira sua chave de API do Alpha Vantage aqui
api_key = 'SUA_CHAVE_DE_API'

# Símbolo da ação que você deseja consultar (por exemplo, 'AAPL' para a Apple)
symbol = 'AAPL'

# Faça uma solicitação para obter os preços históricos da ação
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ao acessar a API do Alpha Vantage.')
