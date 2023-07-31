import pandas as pd
import matplotlib.pyplot as plt


portfolio_ofertas = pd.read_csv('./Datas/portfolio_ofertas.csv', encoding='utf-8')
clientes = pd.read_csv('./Datas/clientes.csv', encoding='utf-8')
ofertas = pd.read_csv('./Datas/ofertas.csv', encoding='utf-8')

plt.figure(figsize=(10,6))
plt.title('Densidade de Idade e Renda Anual dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Renda Anual')
plt.hexbin(clientes['idade'], clientes['renda_anual'], gridsize=20, cmap='inferno')
plt.colorbar()
plt.show()

# Create a bar chart of the count of each tipo_evento for each id_oferta
ofertas.groupby(['id_oferta', 'tipo_evento']).size().unstack().plot(kind='bar', stacked=True)

# Add labels and title
plt.xlabel('ID da Oferta')
plt.ylabel('Contagem')
plt.title('Contagem de Eventos por Oferta')

# Show the plot
plt.show()

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