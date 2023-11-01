import cups

# Caminho do arquivo que você deseja imprimir
file_to_print = "caminho/do/seu/arquivo.pdf"

# Configuração da impressora (substitua pelo nome da sua impressora)
printer_name = "Nome da Impressora"

conn = cups.Connection()
printers = conn.getPrinters()
default_printer = printers[printer_name]

# Imprime o arquivo
job_id = conn.printFile(printer_name, file_to_print, "Seu Trabalho de Impressao", {})
print(f"Trabalho de impressão enviado para {printer_name}, ID: {job_id}")
