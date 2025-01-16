import pandas as pd

# 1. Ler o conjunto de dados para um DataFrame
dataframe = pd.read_csv('heart.csv')
assert dataframe is not None, "O DataFrame não foi carregado corretamente."
print("O DataFrame foi lido corretamente.")

# 2. Verificar as primeiras linhas do DataFrame usando `head()`
print("Primeiras linhas do DataFrame heart.csv:")
print(dataframe.head())

# 3. Verificar as últimas linhas do DataFrame usando `tail()`
print("Últimas linhas do DataFrame heart.csv:")
print(dataframe.tail())

# 4. Verificar as dimensões do DataFrame usando `shape`
print("Dimensões do DataFrame heart.csv:")
print(dataframe.shape)

# 5. Verificar as informações sobre as colunas do DataFrame usando `info()`
print("Informações sobre as colunas do DataFrame heart.csv:")
print(dataframe.info())

# 6. Verificar as estatísticas descritivas básicas do DataFrame usando `describe()`
print("Estatísticas descritivas do DataFrame heart.csv:")
print(dataframe.describe())

# 7. Tem algum dado ausente neste dataset? Se sim, totalize os dados por coluna.
print("Dados ausentes no DataFrame heart.csv:")
dados_ausentes = dataframe.isnull().sum()
if dados_ausentes.sum() > 0:
    print(dados_ausentes)
else:
    print("Não há dados ausentes no DataFrame heart.csv.")

# 8. Selecionar uma coluna específica do DataFrame retornando como um array Numpy
coluna_convertida_para_numpy = dataframe['age'].to_numpy() # .to_numpy() Converte a coluna 'age' do DataFrame em um array Numpy.
print("Conversão da coluna 'age' do DataFrame heart.csv como array Numpy:")
print(coluna_convertida_para_numpy)

# 9. Selecionar duas ou mais colunas específicas do Dataframe retornando como tipo: DataFrame
subset = dataframe[['age', 'chol', 'thalach']]
print("Seleção das colunas 'age', 'chol' e 'thalach':")
print(subset.head())

# 10. Selecionar linhas específicas do DataFrame usando o método ‘loc[]’
linhas_selecionadas = dataframe.loc[1:7]
print("Seleção das linhas específicas (1 a 7) usando loc[]:")
print(linhas_selecionadas)

# 11. Selecionar linhas específicas do DataFrame usando o método “loc[]” com base em uma ou mais condições.
linhas_condicionais = dataframe.loc[(dataframe['age'] > 50) & (dataframe['chol'] < 200) & (dataframe['thalach'] > 150)]

print("Linhas selecionadas nas condições onde 'age' > 50, 'chol' < 200 e 'thalach' > 150:")
if not linhas_condicionais.empty:
    print(linhas_condicionais)
    print(f"Quantidade de linhas encontradas: {len(linhas_condicionais)}")
else:
    print("Nenhuma linha atende às condições especificadas.")
