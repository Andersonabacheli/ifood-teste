import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("data/pedidos_ifood.csv")

# Converter coluna de data
df['data'] = pd.to_datetime(df['data'])
df['mes'] = df['data'].dt.to_period('M').astype(str)  # cria coluna mês para análise mensal

# Gráfico de vendas por produto (mensal)
def grafico_vendas_por_produto():
    vendas = df.groupby(['mes', 'produto']).size().unstack().fillna(0)
    vendas.plot(kind='line', marker='o', figsize=(12, 6))
    plt.title('Vendas por Produto ao Longo dos Meses')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade de Vendas')
    plt.grid(True)
    plt.legend(title="Produto")
    plt.tight_layout()
    plt.show()

# Gráfico de tempo de entrega
def grafico_tempo_entrega():
    tempo = df.groupby('mes')['tempo_entrega'].mean()
    tempo.plot(kind='line', marker='o', color='green', figsize=(10, 6))
    plt.title('Tempo de Entrega Médio por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Tempo Médio de Entrega (min)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Gráfico de faturamento por produto (mensal)
def grafico_faturamento_por_produto():
    faturamento = df.groupby(['mes', 'produto'])['total'].sum().unstack().fillna(0)
    faturamento.plot(kind='line', marker='o', figsize=(12, 6))
    plt.title('Faturamento por Produto ao Longo dos Meses')
    plt.xlabel('Mês')
    plt.ylabel('Faturamento (R$)')
    plt.grid(True)
    plt.legend(title="Produto")
    plt.tight_layout()
    plt.show()

# Produto mais vendido
def produto_mais_vendido():
    produto = df['produto'].value_counts().idxmax()
    print(f'O produto mais vendido foi: {produto}')

# Cliente que mais comprou
def cliente_que_mais_comprou():
    cliente = df['cliente_id'].value_counts().idxmax()
    print(f'O cliente que mais comprou foi: {cliente}')

# Forma de pagamento mais popular
def forma_pagamento_mais_popular():
    forma = df['forma_pagamento'].value_counts().idxmax()
    print(f'A forma de pagamento mais popular foi: {forma}')

# Tempo de entrega médio geral
def tempo_entrega_medio():
    tempo = df['tempo_entrega'].mean()
    print(f'Tempo médio de entrega: {tempo:.2f} minutos')

# Faturamento total
def faturamento_total():
    total = df['total'].sum()
    print(f'Faturamento total: R$ {total:.2f}')

# Executar
grafico_vendas_por_produto()
grafico_tempo_entrega()
grafico_faturamento_por_produto()
produto_mais_vendido()
cliente_que_mais_comprou()
forma_pagamento_mais_popular()
tempo_entrega_medio()
faturamento_total()
