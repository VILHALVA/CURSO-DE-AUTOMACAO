import shutil

# Caminho do arquivo de origem
caminho_origem = "caminho/do/arquivo_origem.txt"

# Caminho do arquivo de destino (novo nome ou diretório)
caminho_destino = "caminho/do/arquivo_destino.txt"

# Move o arquivo de origem para o destino (também pode ser usado para renomear)
shutil.move(caminho_origem, caminho_destino)

print(f"Arquivo {caminho_origem} movido para {caminho_destino}")
