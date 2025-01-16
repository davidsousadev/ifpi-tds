import pandas as pd

# 1. Carregar os Dados: Carregue o conjunto de dados vgsales.csv usando Pandas.
df = pd.read_csv('vgsales.csv')
assert df is not None, "O DataFrame não foi carregado corretamente."
print(f"1 - O DataFrame foi lido corretamente.")

# 2. Visão Geral dos Dados: Exiba as primeiras 5 linhas do DataFrame para obter uma visão geral dos dados.
print("2 - Primeiras 5 linhas do DataFrame:")
print(df.head())

# 2.1
print("2.1 - Últimas 5 linhas do DataFrame:")
print(df.tail())

# 3. Estatísticas Descritivas: Calcule as estatísticas descritivas para as colunas de vendas (NA_Sales, EU_Sales, JP_Sales Other_Sales, Global_Sales).
print("3 - Estatísticas Descritivas das colunas de vendas:")
print(df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].describe().round(2))

# 4. Total de Vendas por Gênero: Calcule o total de vendas globais para cada gênero.
total_vendas_genero = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
print("4 - Total de Vendas Globais por Gênero:")
print(total_vendas_genero)

# 5. Total de Vendas por Plataforma: Calcule o total de vendas globais para cada plataforma.
total_vendas_plataforma = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
print("5 - Total de Vendas Globais por Plataforma:")
print(total_vendas_plataforma)

# 6. Jogo Mais Vendido: Determine qual jogo teve as maiores vendas globais.
jogo_mais_vendido = df.loc[df['Global_Sales'].idxmax()]
print("6 - Jogo com maiores vendas globais:")
print(jogo_mais_vendido)

# 7. Vendas Anuais: Calcule o total de vendas globais para cada ano.
total_vendas_anuais = df.groupby('Year')['Global_Sales'].sum()
print("7 - Total de Vendas Globais por Ano:")
print(total_vendas_anuais)

# 8. Calcule e mostre o total de vendas por gênero e por plataforma
vendas_genero_plataforma = df.groupby(['Genre', 'Platform'])['Global_Sales'].sum().unstack(fill_value=0)
print("8 - Total de Vendas por Gênero e Plataforma:")
print(vendas_genero_plataforma)

# 8.1 - Quantidade de gêneros e plataformas no DataFrame
quantidade_generos = df['Genre'].nunique()
print(f"8.1.1 - Quantidade de gêneros: {quantidade_generos}")
quantidade_plataformas = df['Platform'].nunique()
print(f"8.1.2 - Quantidade de plataformas: {quantidade_plataformas}")

# 8.2 - Gênero mais popular globalmente
genero_popular = total_vendas_genero.idxmax()
print(f"8.2 - O gênero mais popular globalmente é '{genero_popular}', com vendas totais de {total_vendas_genero.max()}.")

# 8.3 - Plataforma com maior diversidade de gêneros
plataforma_diversa = vendas_genero_plataforma.astype(bool).sum(axis=0).idxmax()
print(f"8.3 - A plataforma com maior diversidade de gêneros é '{plataforma_diversa}', com {vendas_genero_plataforma.astype(bool).sum(axis=0).max()} gêneros diferentes.")


