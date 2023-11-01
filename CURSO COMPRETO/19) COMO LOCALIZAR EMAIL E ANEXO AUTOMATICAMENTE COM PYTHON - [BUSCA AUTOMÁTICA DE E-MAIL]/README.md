# COMO LOCALIZAR EMAIL E ANEXO AUTOMATICAMENTE COM PYTHON - [BUSCA AUTOMÁTICA DE E-MAIL]
Para localizar e baixar automaticamente e-mails com anexos usando Python, você pode usar a biblioteca `imaplib`, que permite interagir com protocolos IMAP (Internet Message Access Protocol) para acessar caixas de correio eletrônico. Aqui está um exemplo de como fazer isso:

**Passo 1: Configurar sua Conta de E-mail**

Antes de começar, configure uma conta de e-mail a partir da qual você deseja buscar e baixar e-mails. Certifique-se de que essa conta esteja configurada para permitir acesso IMAP. Geralmente, você precisará ativar essa opção nas configurações de sua conta de e-mail.

**Passo 2: Instalar a biblioteca `imaplib`**

Você não precisa instalar a biblioteca `imaplib` separadamente, pois ela faz parte da biblioteca padrão do Python.

**Passo 3: Escrever o Código Python**

Aqui está um exemplo simples de código Python para localizar e baixar e-mails com anexos:

```python
import imaplib
import email
from email.header import decode_header
import os

# Configurações IMAP
imap_server = 'imap.example.com'  # Substitua pelo servidor IMAP do seu provedor de e-mail
user = 'seu_email@example.com'
password = 'sua_senha'

# Conecte-se ao servidor IMAP
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(user, password)

# Selecionar a caixa de entrada (ou outra pasta)
mail.select('INBOX')

# Pesquisar por e-mails com anexos
status, email_ids = mail.search(None, 'ALL')

# Recuperar os IDs dos e-mails
email_id_list = email_ids[0].split()
for email_id in email_id_list:
    status, email_data = mail.fetch(email_id, '(RFC822)')
    raw_email = email_data[0][1]

    # Analisar o e-mail
    msg = email.message_from_bytes(raw_email)

    # Verificar se o e-mail tem anexos
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            # Baixar o anexo
            filename = part.get_filename()
            filename = decode_header(filename)[0][0].decode()
            if filename:
                print(f'Baixando anexo: {filename}')
                with open(filename, 'wb') as attachment:
                    attachment.write(part.get_payload(decode=True))

# Fechar a conexão
mail.logout()
```

Lembre-se de substituir `'imap.example.com'`, `'seu_email@example.com'` e `'sua_senha'` pelas configurações IMAP do seu provedor de e-mail e suas credenciais. Certifique-se de que sua conta de e-mail permita o acesso IMAP.

Este código faz o seguinte:

1. Conecta-se ao servidor IMAP do seu provedor de e-mail.
2. Seleciona a caixa de entrada.
3. Pesquisa por todos os e-mails na caixa de entrada.
4. Itera pelos e-mails encontrados e verifica se eles têm anexos.
5. Baixa qualquer anexo encontrado e o salva no diretório de trabalho.

Lembre-se de que este é um exemplo simples e pode ser personalizado para atender às suas necessidades específicas. Certifique-se de entender as configurações de segurança necessárias e as permissões de acesso à caixa de entrada da sua conta de e-mail.