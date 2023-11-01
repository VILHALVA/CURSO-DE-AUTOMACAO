import smtplib
import schedule
import time

# Função para enviar um e-mail de alerta
def enviar_alerta():
    # Configurações do servidor de e-mail (substitua com suas informações)
    smtp_server = 'smtp.seuemail.com'
    smtp_port = 587
    email_de = 'seu_email@gmail.com'
    senha = 'sua_senha'

    # Configurações do e-mail
    destinatario = 'destinatario@email.com'
    assunto = 'Alerta Automático'
    mensagem = 'Este é um alerta automático enviado por Python.'

    # Conectar-se ao servidor de e-mail
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_de, senha)

    # Criar e enviar o e-mail
    email = f'Subject: {assunto}\n\n{mensagem}'
    server.sendmail(email_de, destinatario, email)

    # Fechar a conexão com o servidor de e-mail
    server.quit()
    print("E-mail de alerta enviado!")

# Agendar o envio de e-mail de alerta
schedule.every().day.at("10:00").do(enviar_alerta)

# Loop principal para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)
