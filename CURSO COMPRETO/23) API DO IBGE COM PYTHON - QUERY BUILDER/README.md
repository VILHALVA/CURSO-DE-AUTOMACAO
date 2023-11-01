# API DO IBGE COM PYTHON - QUERY BUILDER
O Instituto Brasileiro de Geografia e Estatística (IBGE) oferece uma API RESTful que permite acessar dados geoespaciais, econômicos e demográficos do Brasil. Para acessar a API do IBGE com Python, você pode usar a biblioteca `requests` para fazer solicitações HTTP e consultar os dados desejados.

O IBGE disponibiliza uma ferramenta chamada "Query Builder" que facilita a construção de consultas personalizadas para diferentes conjuntos de dados. A seguir, um exemplo de como usar a API do IBGE com Python e o "Query Builder" para acessar dados de municípios brasileiros.

**Passo 1: Instalar a biblioteca `requests`**

Certifique-se de que você tenha a biblioteca `requests` instalada. Se ainda não a tiver, você pode instalá-la com o seguinte comando:

```bash
pip install requests
```

**Passo 2: Consultar dados do IBGE com Python**

Aqui está um exemplo de como consultar dados geoespaciais do IBGE usando o "Query Builder" e a biblioteca `requests`:

```python
import requests

# URL da consulta da API do IBGE (substitua com a sua consulta)
url = "https://servicodados.ibge.gov.br/api/v2/malhas/BR?formato=application/vnd.geo+json&qualidade=5"

# Realize a solicitação HTTP GET
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Os dados estão no formato GeoJSON
    dados_geojson = response.json()
    # Agora você pode processar os dados conforme necessário
    print(dados_geojson)
else:
    print("Falha na solicitação da API do IBGE.")
```

Neste exemplo, o URL da consulta foi definido para recuperar os limites geográficos dos municípios brasileiros em formato GeoJSON. Você pode personalizar a consulta conforme suas necessidades, usando a ferramenta "Query Builder" do IBGE para gerar URLs de consulta específicos.

Além disso, o IBGE fornece outros conjuntos de dados, como dados econômicos e demográficos. Você pode utilizar a mesma abordagem para acessar esses dados, ajustando o URL de consulta de acordo com o conjunto de dados que deseja.

Certifique-se de verificar a documentação oficial do IBGE para obter mais detalhes sobre os conjuntos de dados disponíveis e como construir consultas personalizadas: [API do IBGE](https://servicodados.ibge.gov.br/api/docs).