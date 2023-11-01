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
