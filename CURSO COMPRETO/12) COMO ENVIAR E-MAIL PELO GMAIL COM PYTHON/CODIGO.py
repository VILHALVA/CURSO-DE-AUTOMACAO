import smtplib
import email

# Defina as credenciais de e-mail
email_address = "seu_endereço_de_email"
email_password = "sua_senha"

# Crie uma mensagem de e-mail
message = email.message.Message()
message["Subject"] = "Assunto do e-mail"
message["From"] = email_address
message["To"] = "destinatário@email.com"
message.set_content("Corpo do e-mail")

# Envie a mensagem de e-mail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_address, email_password)
server.sendmail(email_address, "destinatário@email.com", message.as_string())
server.quit()
