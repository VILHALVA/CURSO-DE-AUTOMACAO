import win32print
import win32ui

# Nome da impressora (substitua pelo nome da sua impressora)
printer_name = "Nome da Impressora"

# Caminho do arquivo que você deseja imprimir
file_to_print = "caminho/do/seu/arquivo.pdf"

# Abre a impressora
printer = win32print.OpenPrinter(printer_name)

# Configura a impressão
printer_info = win32print.GetPrinter(printer, 2)
pdc = win32ui.CreateDC()
pdc.CreatePrinterDC(printer_name)
pdc.StartDoc('Documento de Impressao')
pdc.StartPage()
pdc.SetMapMode(3)  # MM_LOMETRIC

# Abre o arquivo a ser impresso
file = open(file_to_print, 'rb')
data = file.read()
file.close()

# Imprime o conteúdo do arquivo
pdc.TextOut(100, 100, data)

# Finaliza a impressão
pdc.EndPage()
pdc.EndDoc()
pdc.DeleteDC()
win32print.ClosePrinter(printer)
