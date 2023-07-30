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

ofertas.groupby(['renda_anual', 'tipo_evento']).size().unstack().plot(kind='bar', stacked=True)

plt.xlabel('Renda Anual')
plt.ylabel('Tipo de Evento')
plt.title('Renda Anual x Tipo de Evento')

plt.show()

