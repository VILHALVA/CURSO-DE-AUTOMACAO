# COMO COPIAR E MOVER ARQUIVOS DO COMPUTADOR COM PYTHON?
Para copiar e mover arquivos no computador usando Python, você pode usar a biblioteca `shutil`, que fornece funções para operações de manipulação de arquivos e diretórios, como cópia e movimentação. Abaixo estão exemplos de como copiar e mover arquivos:

**Copiar um arquivo:**

```python
import shutil

# Caminho do arquivo de origem
caminho_origem = "caminho/do/arquivo_origem.txt"

# Caminho do arquivo de destino
caminho_destino = "caminho/do/arquivo_destino.txt"

# Copia o arquivo de origem para o destino
shutil.copy(caminho_origem, caminho_destino)

print(f"Arquivo {caminho_origem} copiado para {caminho_destino}")
```

**Mover (renomear) um arquivo:**

```python
import shutil

# Caminho do arquivo de origem
caminho_origem = "caminho/do/arquivo_origem.txt"

# Caminho do arquivo de destino (novo nome ou diretório)
caminho_destino = "caminho/do/arquivo_destino.txt"

# Move o arquivo de origem para o destino (também pode ser usado para renomear)
shutil.move(caminho_origem, caminho_destino)

print(f"Arquivo {caminho_origem} movido para {caminho_destino}")
```

Lembre-se de substituir `"caminho/do/arquivo_origem.txt"` e `"caminho/do/arquivo_destino.txt"` pelos caminhos dos arquivos de origem e destino em seu sistema. Você pode usar essas funções para realizar operações de cópia ou movimentação de arquivos em seu sistema de arquivos local.

Certifique-se de que a pasta de destino exista antes de mover ou copiar o arquivo, e que você tenha as permissões adequadas para acessar e modificar os arquivos e diretórios envolvidos.

A biblioteca `shutil` também oferece funções para copiar e mover diretórios inteiros. Certifique-se de consultar a documentação oficial do Python para obter mais informações sobre o uso da biblioteca `shutil`.