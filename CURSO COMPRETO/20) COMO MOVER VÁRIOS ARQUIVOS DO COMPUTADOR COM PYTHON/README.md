# COMO MOVER VÁRIOS ARQUIVOS DO COMPUTADOR COM PYTHON
Para mover vários arquivos do computador usando Python, você pode utilizar a biblioteca `shutil`, que fornece várias funções úteis para operações de manipulação de arquivos e diretórios. Aqui está um exemplo de como mover arquivos de um diretório de origem para um diretório de destino:

```python
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
```

Certifique-se de personalizar os valores das variáveis `diretorio_origem` e `diretorio_destino` para corresponder aos caminhos dos diretórios de origem e destino em seu sistema. A lista `arquivos_a_mover` contém os nomes dos arquivos que você deseja mover.

Este exemplo iterará sobre a lista de arquivos e moverá cada um deles do diretório de origem para o diretório de destino. Certifique-se de que os diretórios de origem e destino existam e que os arquivos a serem movidos também existam no diretório de origem.

Lembre-se de que a biblioteca `shutil` oferece outras funcionalidades úteis para operações de arquivo, como cópia, renomeação e exclusão, além da movimentação de arquivos. Certifique-se de consultar a documentação oficial do Python para obter mais informações sobre o uso da biblioteca `shutil`.