import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Carregue as credenciais da conta de serviço a partir do arquivo JSON
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Substitua 'sua-chave-de-acesso.json' pelo caminho do seu arquivo JSON de credenciais
credentials = ServiceAccountCredentials.from_json_keyfile_name('sua-chave-de-acesso.json', scope)

# Autentique-se com a API
gc = gspread.authorize(credentials)

# Abra a planilha pelo nome
planilha = gc.open('Nome da Sua Planilha')

# Acesse uma folha específica
folha = planilha.worksheet('Nome da Sua Folha')

# Leia dados da planilha
dados = folha.get_all_values()

# Imprima os dados
for linha in dados:
    print(linha)

# Atualize um valor na planilha (por exemplo, na célula A1)
folha.update('A1', 'Novo Valor')
