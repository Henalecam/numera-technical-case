# BEGIN: 7x3zv9c5d2j1
import pandas as pd
import matplotlib.pyplot as plt

portfolio_ofertas = pd.read_csv('./Datas/portfolio_ofertas.csv', encoding='utf-8')
clientes = pd.read_csv('./Datas/clientes.csv', encoding='utf-8')
ofertas = pd.read_csv('./Datas/ofertas.csv', encoding='utf-8')

# Filter the data by gender
clientes_f = clientes[clientes['genero'] == 'F']
clientes_m = clientes[clientes['genero'] == 'M']


plt.figure(figsize=(10, 6))
plt.title('Density of Annual Income by Gender')
plt.xlabel('Annual Income')
plt.ylabel('Density')
plt.hist(clientes_f['renda_anual'], density=True, alpha=0.5, label='Female')
plt.hist(clientes_m['renda_anual'], density=True, alpha=0.5, label='Male')
plt.ticklabel_format(style='plain', axis='y') # Remove scientific notation
plt.legend()
plt.show()
