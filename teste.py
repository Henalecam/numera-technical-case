
# BEGIN: 7x3zv9c5d2j1
import pandas as pd
import matplotlib.pyplot as plt

portfolio_ofertas = pd.read_csv('./Datas/portfolio_ofertas.csv', encoding='utf-8')
clientes = pd.read_csv('./Datas/clientes.csv', encoding='utf-8')
ofertas = pd.read_csv('./Datas/ofertas.csv', encoding='utf-8')

# Merge clientes with ofertas based on id_cliente column
ofertas = pd.merge(ofertas, clientes[['id', 'renda_anual']], left_on='cliente', right_on='id')


grouped_data = ofertas.groupby(['renda_anual', 'tipo_evento']).size().unstack()

# Plot the grouped data with a line plot
grouped_data.plot(kind='line', marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Renda Anual')
plt.ylabel('Densidade')
plt.title('Renda Anual x Tipo de Evento')

plt.legend(title='Tipo de Evento', loc='upper left')  # Show legend with event types

plt.grid(True)  # Add grid lines for better readability

plt.show()