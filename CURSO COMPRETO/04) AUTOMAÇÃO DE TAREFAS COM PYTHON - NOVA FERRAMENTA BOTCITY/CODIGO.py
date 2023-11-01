import smtplib

def send_email(to_email, subject, body):
    # Crie uma conexão SMTP com o servidor de e-mail
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("seu_endereço_de_email", "sua_senha")

        # Crie uma mensagem de e-mail
        message = "Subject: {subject}\n\n{body}".format(
            subject=subject, body=body
        )

        # Envie a mensagem de e-mail
        smtp.sendmail("seu_endereço_de_email", to_email, message)

# Chame a função para enviar um e-mail para cada cliente
for customer in customers:
    send_email(customer["email"], "Assunto do e-mail", "Corpo do e-mail")