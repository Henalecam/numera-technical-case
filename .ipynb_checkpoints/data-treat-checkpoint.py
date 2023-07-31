import pandas as pd
import matplotlib.pyplot as plt

portfolio_ofertas = pd.read_csv('./Datas/portfolio_ofertas.csv')
clientes = pd.read_csv('./Datas/clientes.csv')
ofertas = pd.read_csv('./Datas/ofertas.csv')

# Replace all 'oferta concluída' to 'oferta concluida' in the 'tipo_evento' column
ofertas['tipo_evento'] = ofertas['tipo_evento'].str.replace('oferta conclu�da', 'oferta concluida')

