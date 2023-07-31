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


# * Gráfico de Renda Anual X Idade - Com densidade
plt.figure(figsize=(10,6))
plt.title('Densidade de Idade e Renda Anual dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Renda Anual')
plt.hexbin(clientes['idade'], clientes['renda_anual'], gridsize=20, cmap='inferno')
plt.colorbar().set_label('Densidade')
plt.show()

# * Gráfico de Contagem de eventos por Oferta
ofertas.groupby(['id_oferta', 'tipo_evento']).size().unstack().plot(kind='bar', stacked=True)

plt.xlabel('ID da Oferta')
plt.ylabel('Contagem')
plt.title('Contagem de Eventos por Oferta')

plt.show()

# * Gráfico de Renda Anual X Tipo Evento - Com densidade

ofertas = pd.merge(ofertas, clientes[['id', 'renda_anual']], left_on='cliente', right_on='id')

grouped_data = ofertas.groupby(['renda_anual', 'tipo_evento']).size().unstack()

grouped_data.plot(kind='line', marker='o', linestyle='-')

plt.xlabel('Renda Anual')
plt.ylabel('Densidade')
plt.title('Renda Anual x Tipo de Evento')

plt.legend(title='Tipo de Evento', loc='upper left')

plt.grid(True)

plt.show()


# * Gráfico de renda por Genero - Com densidade

plt.figure(figsize=(10, 6))
plt.title('Densidade de renda por sexo')
plt.xlabel('Renda Anual')
plt.ylabel('Densidade')
plt.hist(clientes_f['renda_anual'], density=True, alpha=0.5, label='Mulher')
plt.hist(clientes_m['renda_anual'], density=True, alpha=0.5, label='Homem')
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.show()

# * Gráfico de renda por idade dos top 1000

plt.figure(figsize=(10,6))
plt.title('Densidade de Idade e Renda Anual dos Clientes top 1000 recompensa')
plt.xlabel('Idade')
plt.ylabel('Renda Anual')
plt.hexbin(clientes_top_1000['idade'], clientes_top_1000['renda_anual'], gridsize=20, cmap='viridis')
plt.colorbar().set_label('Densidade')
plt.show()