import os

# Diretório que você deseja verificar
diretorio = '/caminho/do/seu/diretorio'

# Listar todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Filtrar apenas os arquivos (excluindo diretórios)
arquivos = [os.path.join(diretorio, arquivo) for arquivo in arquivos if os.path.isfile(os.path.join(diretorio, arquivo))]

# Verificar se há arquivos no diretório
if not arquivos:
    print("O diretório está vazio.")
else:
    # Encontre o arquivo mais recente com base na data de modificação
    arquivo_mais_recente = max(arquivos, key=os.path.getmtime)

    # Obtenha a data de modificação do arquivo mais recente
    data_modificacao = os.path.getmtime(arquivo_mais_recente)

    # Imprima o caminho do arquivo mais recente e sua data de modificação
    print(f"Arquivo mais recente: {arquivo_mais_recente}")
    print(f"Data de modificação: {data_modificacao}")
