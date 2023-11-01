import yfinance as yf
import pandas as pd

# Defina o símbolo da ação que você deseja consultar (por exemplo, Apple)
acao = 'AAPL'

# Crie um objeto Ticker para obter os dados da ação
acao_info = yf.Ticker(acao)

# Obtenha informações resumidas da ação
resumo = acao_info.info
print(f"Informações sobre a ação {acao}:\n")
print(resumo)

# Obtenha histórico de preços de fechamento para a ação
historico = acao_info.history(period="1d")
print(f"\nHistórico de preços de fechamento para {acao}:\n")
print(historico)

# Obtenha informações sobre dividendos
dividendos = acao_info.dividends
print(f"\nDividendos para {acao}:\n")
print(dividendos)
