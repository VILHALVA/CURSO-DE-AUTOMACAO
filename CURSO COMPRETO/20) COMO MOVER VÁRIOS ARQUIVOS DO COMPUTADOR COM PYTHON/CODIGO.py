import shutil
import os

# Diretório de origem
diretorio_origem = "/caminho/do/diretorio_de_origem"

# Diretório de destino
diretorio_destino = "/caminho/do/diretorio_de_destino"

# Lista de arquivos a serem movidos (você pode personalizar esta lista)
arquivos_a_mover = ["arquivo1.txt", "arquivo2.jpg", "arquivo3.pdf"]

# Iterar sobre os arquivos e movê-los
for arquivo in arquivos_a_mover:
    origem_arquivo = os.path.join(diretorio_origem, arquivo)
    destino_arquivo = os.path.join(diretorio_destino, arquivo)

    # Verificar se o arquivo de origem existe antes de movê-lo
    if os.path.exists(origem_arquivo):
        shutil.move(origem_arquivo, destino_arquivo)
        print(f"Movido: {arquivo} de {diretorio_origem} para {diretorio_destino}")
    else:
        print(f"O arquivo {arquivo} não existe em {diretorio_origem}")

print("Todos os arquivos foram movidos.")
