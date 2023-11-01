import schedule
import time

# Função para a tarefa a ser agendada
def minha_tarefa():
    print("Tarefa agendada executada!")

# Agendar a tarefa para ser executada a cada dia às 10:00
schedule.every().day.at("10:00").do(minha_tarefa)

# Loop principal para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)
