import pandas as pd

# 1. Ler o conjunto de dados para um DataFrame
arquivo = "202005.CSV"
df = pd.read_csv(arquivo, sep=";", decimal=",")
assert df is not None, "O DataFrame não foi carregado corretamente."
print(f"1 - O DataFrame '{arquivo}' foi lido corretamente.")

# 2. Verificar as primeiras linhas do DataFrame usando `head()`
print(f"2 - Primeiras linhas do DataFrame de {arquivo}:")
print(df.head())

# 3. Verificar as últimas linhas do DataFrame usando `tail()`
print(f"3 - Últimas linhas do DataFrame de {arquivo}:")
print(df.tail())

# 4. Verificar as dimensões do DataFrame usando `shape`
print(f"4 - Dimensões do DataFrame de {arquivo}:")
print(f"Dimensões: {df.shape}")

# 5. Verificar as informações sobre as colunas do DataFrame usando `info()`
print("5 - Informações sobre as colunas:")
print(df.info())

# 6. Verificar as estatísticas descritivas básicas do DataFrame usando `describe()`
print("6 - Estatísticas descritivas básicas:")
print(df.describe())

# 7. Selecionar colunas específicas do DataFrame usando colchetes `[]` ou o método `loc[]`
colunas_especificas = df[['Ano de Referência', 'Mês de Referência', 'ICAO Empresa Aérea', 'Tarifa-N']]
print("7 - Colunas selecionadas:")
print(colunas_especificas.head())

# Insight 7: Empresas com as tarifas médias mais altas no ano
tarifa_media_por_empresa = colunas_especificas.groupby('ICAO Empresa Aérea')['Tarifa-N'].mean().round(2).sort_values(ascending=False)
print("7.1 - Tarifas médias por empresa aérea:")
print(tarifa_media_por_empresa)

# 8. Selecionar linhas específicas do DataFrame usando o método `loc[]`
df_maio_azu = df.loc[(df['ICAO Empresa Aérea'] == 'AZU') & (df['Tarifa-N'] < 200)]
print("8 - Dados para a empresa AZU:")
print(df_maio_azu)

# Insight 8: Média da tarifa da empresa AZU
tarifa_media_maio_azu = df_maio_azu['Tarifa-N'].mean().round(2)
print(f"8.1 - Média da tarifa da AZU: {tarifa_media_maio_azu}")

# 9. Filtre linhas do Dataframe com base em uma condição usando operadores lógicos '&' e '|'
voos_baratos = df.loc[df['Tarifa-N'] < 100]
print("9 - Voos com tarifas abaixo de R$100:")
print(voos_baratos)

# Insight 9: Percentual de voos com tarifas abaixo de R$100
if len(df) > 0:
    percentual_baratos = len(voos_baratos) / len(df) * 100
    print(f"9.1 - Percentual de voos com tarifas abaixo de R$100: {percentual_baratos:.2f}%")
else:
    print("9.1 - O DataFrame está vazio. Não é possível calcular o percentual.")

# 10. Agrupar dados do dataframe com base em uma ou mais colunas usando o método  'group by()'
empresa_com_mais_voos_sbae = df[df['ICAO Aeródromo Origem'] == 'SBAE'].groupby('ICAO Empresa Aérea').size().sort_values(ascending=False)
if not empresa_com_mais_voos_sbae.empty:
    print("10 - Empresa com mais voos partindo do aeródromo SBAE:")
    print(empresa_com_mais_voos_sbae)
else:
    print("10 - Nenhum voo encontrado com origem em SBAE.")

# Insight 10.1
if not empresa_com_mais_voos_sbae.empty:
    maior_empresa = empresa_com_mais_voos_sbae.idxmax()
    print(f"10.1 - Empresa com mais voos partindo de SBAE: {maior_empresa} com {empresa_com_mais_voos_sbae.max()} voos.")
else:
    print("10.1 - Nenhum voo encontrado com origem em SBAE.")

# 11. Ordenar o dataframe com base em uma ou mais colunas usando o método: sort_values()
df_sorted = df.sort_values(by='Tarifa-N', ascending=False)
print("11 - DataFrame ordenado pelas tarifas (decrescente):")
print(df_sorted)

# Insight 11: Voo mais caro do mês
voo_mais_caro = df_sorted.iloc[0]
print("11.1 - Detalhes do voo mais caro:")
for coluna, valor in voo_mais_caro.items():
    print(f"  {coluna}: {valor}")
