# API DE PREÇO DE AÇÕES E INFORMAÇÕES ECONÔMICAS COM PYTHON
Para obter informações de preços de ações e dados econômicos usando Python, você pode usar várias APIs e bibliotecas de terceiros. Duas fontes populares de dados são o Alpha Vantage para preços de ações e o Quandl para dados econômicos. Aqui estão os passos gerais para acessar essas informações usando Python:

**1. Alpha Vantage API para Preços de Ações:**

O Alpha Vantage fornece uma API gratuita para obter informações de preços de ações. Primeiro, você precisa se inscrever no Alpha Vantage para obter uma chave de API.

**Instale a biblioteca requests** para fazer solicitações HTTP à API:

```bash
pip install requests
```

**Exemplo de uso do Alpha Vantage API:**

```python
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
```

**2. Quandl API para Dados Econômicos:**

O Quandl é uma plataforma que fornece dados econômicos e financeiros. Você também precisará de uma chave de API do Quandl para acessar seus dados.

**Instale a biblioteca requests** como mencionado anteriormente, e você pode usar sua chave de API do Quandl para acessar os dados.

**Exemplo de uso do Quandl API:**

```python
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
```

Lembre-se de que esses são exemplos simples de como acessar informações de preços de ações e dados econômicos. Você pode personalizar as solicitações de acordo com suas necessidades e formatar os dados para análise. Além disso, existem outras bibliotecas em Python, como Pandas, para trabalhar com os dados de forma mais eficaz. Certifique-se de ler a documentação das APIs (Alpha Vantage e Quandl) para obter detalhes sobre os endpoints disponíveis e as opções de consulta.