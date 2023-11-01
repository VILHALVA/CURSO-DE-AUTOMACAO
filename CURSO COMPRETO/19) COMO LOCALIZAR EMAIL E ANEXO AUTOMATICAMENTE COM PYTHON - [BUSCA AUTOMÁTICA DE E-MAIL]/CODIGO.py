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
