# API DO GOOGLESHEETS COM PYTHON
Para trabalhar com a API do Google Sheets em Python, você precisa utilizar a biblioteca oficial do Google, chamada `gspread`. Aqui estão os passos gerais para configurar e usar a API do Google Sheets com Python:

**Passo 1: Configurar um Projeto no Console de Desenvolvedores do Google:**

1. Acesse [https://console.developers.google.com/](https://console.developers.google.com/).
2. Crie um novo projeto ou selecione um projeto existente.
3. No painel do projeto, vá para "APIs & Services" > "Library".
4. Pesquise e ative a "Google Sheets API".
5. No painel esquerdo, clique em "Credenciais" e depois em "Create credentials".
6. Selecione "Service Account Key" e siga as etapas para criar uma conta de serviço e uma chave de acesso. Você também precisará atribuir a função apropriada, como "Editor" ou "Visualizador" para acessar as planilhas.
7. Baixe a chave JSON (seu arquivo de chave) que contém informações de autenticação.

**Passo 2: Compartilhar a Planilha com o Email da Conta de Serviço:**

Na planilha que você deseja acessar, compartilhe-a com o endereço de e-mail da conta de serviço que você criou no passo anterior. Isso permitirá que a conta de serviço acesse a planilha.

**Passo 3: Instalar a Biblioteca `gspread` e Autenticar com a Conta de Serviço:**

1. Instale a biblioteca `gspread` usando o `pip`:

   ```bash
   pip install gspread
   ```

2. Carregue a chave de acesso (arquivo JSON) que você baixou do Console de Desenvolvedores e autentique-se com a API:

   ```python
   import gspread
   from oauth2client.service_account import ServiceAccountCredentials

   # Carregue as credenciais da conta de serviço do JSON
   scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

   credentials = ServiceAccountCredentials.from_json_keyfile_name(
       'sua-chave-de-acesso.json', scope)

   # Autentique-se com a API
   gc = gspread.authorize(credentials)
   ```

**Passo 4: Acessar e Trabalhar com a Planilha:**

Agora você pode usar a biblioteca `gspread` para abrir e manipular a planilha:

```python
# Abra a planilha por nome
planilha = gc.open('Nome da Sua Planilha')

# Acesse uma folha específica
folha = planilha.worksheet('Nome da Sua Folha')

# Leia dados da planilha
dados = folha.get_all_values()

# Atualize a planilha
folha.update('A1', 'Novo Valor')
```

Isso é um exemplo básico de como acessar uma planilha do Google Sheets com Python. Você pode fazer muitas outras operações, como adicionar, modificar ou excluir dados da planilha. Consulte a documentação do `gspread` para obter mais detalhes e exemplos: [Documentação do gspread](https://gspread.readthedocs.io/en/latest/).