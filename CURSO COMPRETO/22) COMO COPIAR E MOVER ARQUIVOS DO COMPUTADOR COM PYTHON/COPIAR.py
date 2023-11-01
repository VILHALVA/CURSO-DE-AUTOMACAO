import shutil

# Caminho do arquivo de origem
caminho_origem = "caminho/do/arquivo_origem.txt"

# Caminho do arquivo de destino
caminho_destino = "caminho/do/arquivo_destino.txt"

# Copia o arquivo de origem para o destino
shutil.copy(caminho_origem, caminho_destino)

print(f"Arquivo {caminho_origem} copiado para {caminho_destino}")
