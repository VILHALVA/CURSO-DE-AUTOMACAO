import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor de e-mail
smtp_server = 'smtp.gmail.com'  # Use o servidor SMTP adequado (por exemplo, para o Gmail)
smtp_port = 587  # Porta padrão para TLS

# Seu endereço de e-mail e senha
sender_email = 'seu_email@gmail.com'
sender_password = 'sua_senha'

# Destinatário
recipient_email = 'destinatario@email.com'

# Crie a mensagem
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Assunto do E-mail'

# Corpo do e-mail
body = 'Este é o corpo do e-mail de notificação automática.'
message.attach(MIMEText(body, 'plain'))

# Conecte-se ao servidor de e-mail e envie a mensagem
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
    print('E-mail de notificação enviado com sucesso.')
except Exception as e:
    print(f'Erro ao enviar o e-mail: {str(e)}')
