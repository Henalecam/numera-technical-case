# BEGIN: 7x3zv9c5d2j1
import pandas as pd
import matplotlib.pyplot as plt

portfolio_ofertas = pd.read_csv('./Datas/portfolio_ofertas.csv', encoding='utf-8')
clientes = pd.read_csv('./Datas/clientes.csv', encoding='utf-8')
ofertas = pd.read_csv('./Datas/ofertas.csv', encoding='utf-8')

# * Filtra Homem e mulher em grupos separados

clientes_f = clientes[clientes['genero'] == 'F']
clientes_m = clientes[clientes['genero'] == 'M']

ofertas_clientes = pd.merge(ofertas, clientes, left_on='cliente', right_on='id')

# * soma de recompensas por id
recompensas_por_id = ofertas.groupby('cliente')['recompensa'].sum()

# * Os 1000 maiores acumuladores de recompensa
top_1000_ids = recompensas_por_id.nlargest(1000).index.tolist()
clientes_top_1000 = clientes[clientes['id'].isin(top_1000_ids)]

# * Gráfico de torta que mostra a % de homens e mulheres
sizes = [len(clientes_f), len(clientes_m)]
labels = ['Mulheres', 'Homens']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Distribuição de gênero')
plt.show()
