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
