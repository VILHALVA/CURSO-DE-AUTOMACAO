# API DE CEP E BUSCA DE ENDEREÇOS COM PYTHON
Para realizar buscas de endereços a partir de CEPs usando Python, você pode utilizar a API de CEPs oferecida por diferentes serviços. Um serviço popular é o ViaCEP, que fornece dados de endereços brasileiros com base no CEP. Abaixo, vou mostrar como você pode realizar consultas de endereços usando o ViaCEP em Python.

**Passo 1: Instalar a biblioteca `requests`**

Você deve ter a biblioteca `requests` instalada para fazer solicitações HTTP à API do ViaCEP. Se você ainda não a tiver instalado, pode fazê-lo com o seguinte comando:

```bash
pip install requests
```

**Passo 2: Escrever o Código Python para Consulta de CEPs**

Aqui está um exemplo de código Python que consulta e exibe informações de endereços a partir de um CEP usando o serviço ViaCEP:

```python
import requests

# Função para consultar informações de endereço a partir de um CEP
def consultar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    if response.status_code == 200:
        dados_endereco = response.json()
        return dados_endereco
    else:
        return None

# Exemplo de uso
cep = "01311-000"  # Substitua pelo CEP desejado
endereco = consultar_endereco_por_cep(cep)

if endereco is not None:
    print(f"CEP: {endereco['cep']}")
    print(f"Logradouro: {endereco['logradouro']}")
    print(f"Complemento: {endereco['complemento']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['localidade']}")
    print(f"Estado: {endereco['uf']}")
else:
    print(f"Não foi possível obter informações para o CEP: {cep}")
```

Neste exemplo, a função `consultar_endereco_por_cep` faz uma solicitação HTTP ao ViaCEP com o CEP fornecido e retorna os dados do endereço, incluindo logradouro, complemento, bairro, cidade e estado. Certifique-se de substituir o valor de `cep` pela entrada do CEP desejado.

O ViaCEP é apenas um dos serviços que fornecem informações de endereço com base em CEPs. Existem outros serviços disponíveis, e você pode escolher o que melhor atenda às suas necessidades.

Lembre-se de que as políticas de uso de serviços de CEP podem variar, então consulte a documentação do serviço escolhido para obter mais informações sobre limitações e políticas de uso.