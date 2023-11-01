import schedule
import time

# Função para a tarefa a ser agendada
def tarefa_diaria():
    print("Esta tarefa será executada diariamente.")

def tarefa_hora():
    print("Esta tarefa será executada a cada hora.")

def tarefa_semanal():
    print("Esta tarefa será executada semanalmente.")

# Agendar tarefa diária
schedule.every().day.at("12:00").do(tarefa_diaria)

# Agendar tarefa a cada hora
schedule.every().hour.do(tarefa_hora)

# Agendar tarefa semanalmente (segunda-feira às 9:00)
schedule.every().monday.at("09:00").do(tarefa_semanal)

# Loop principal para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)
