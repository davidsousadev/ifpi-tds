## Dataset: Arquivo: carros.csv
# 1. subir o arquivo para o notebook -> github
# https://github.com/davidsousadev/ifpi-tds/blob/main/terceiro-periodo/tep/2025-01-15/carros.csv

# 2. importar a biblioteca Pandas
import pandas as pd

import datetime

# 3. carregar o arquivo .csv: criar uma variável dataset que receberá a chamada de **pd.read_csv(arquivo)** Não esquecer do separador ";"
arquivo = 'carros.csv'
df = pd.read_csv(arquivo, sep=';') # Separador ';'

# 4. Mostrar o dataset
print("4 - Dataset:")
print(df)

# 5. mostre os tipos de dados do dataset: comando: dtypes. 
print("5 - Tipos de dados:")
print(df.dtypes)
print("""5.1 - Quais os tipos de dados das colunas deste dataset?
     Tipos: object, int64, float64, bool
""")

# 6. mostre a estatística descritiva das colunas: quilometragem e valor. Qual o significado dessas informações?
print("6 - Estatísticas descritivas - Quilometragem e Valor:")
print(df[['Quilometragem', 'Valor']].describe().round(2))
print("""
      6.1 - Qual o significado dessas informações?
      R: Está exibindo dados pertinentes aos filtros como a quantidade não nula, média dos valores, o desvio padrão e a variação entre valores mínimos, percentuais e valores máximos.
      """)


# 7. Obtenha mais informações do dataset com a função info(). Tem alguma coluna com dados nulos? Se sim, qual a coluna e quantos  dados nulos possui?
print("7 - Informações do Dataset:")
print(df.info())

print("7.1 - Tem alguma coluna com dados nulos?")
if len(df.isnull().sum())>=1:
    print("R: Sim!")
    print("Dados Nulos:")
    print(df.isnull().sum())
else:
    print("R: Não!")

# 8. Com base no Dataset que estamos trabalhando, defina uma função para mostrar a quilometragem média de todos os carros.  Sabendo  que a formula é:
# Km_media = km_total / (ano_atual - ano_fabricação)
# A função tem que receber como parâmetros: o dataset e o ano atual.
# Execute a função e mostre o resultado.

def calcular_km_media(dataset, ano_atual):
    dataset['Km_media'] = dataset['Quilometragem'] / (ano_atual - dataset['Ano'])
    return dataset['Km_media'].mean()

ano_atual = datetime.date.today().year
km_media = calcular_km_media(df, ano_atual)
print(f"8 - Quilometragem média de todos os carros: {km_media:.2f}")

# 9. Utilizando a pesquisa com queries, faça:
# a) mostre os carros com motor "Diesel V8"
print("9.a - Carros com 'Motor Diesel V8':")
print(df.query("Motor == 'Motor Diesel V8'"))

# b) pesquise por carros com motor 1.0 8v usados com preço inferior a R$ 100.000
print("9.b - Carros com 'Motor 1.0 8v' usados e preço < R$ 100.000:")
print(df.query("Motor == 'Motor 1.0 8v' and Zero_km == False and Valor < 100000"))

# c) pesquise por carros com km média de até 10.000 km com Motor 1.8 16v
print("9.c - Carros com Km média até 10.000 km e 'Motor 1.8 16v':")
df.Km_media = df.Quilometragem / (ano_atual - df.Ano)
print(df.query("Km_media <= 10000 and Motor == 'Motor 1.8 16v'"))

# d) liste os tipos de motores cadastrados 
print("9.d - Tipos de motores cadastrados:")
print(df.Motor.unique())

# e) liste os carros com câmbio automático com valor abaixo de R$ 100.000
print("9.e - Carros com câmbio automático e valor < R$ 100.000:")
print(df.query("Valor < 100000 and Acessórios.str.contains('Câmbio automático')"))

# f) liste os carros novos com "freios ABS" que custam acima de R$ 100.000
print("9.f - Carros novos com 'freios ABS' e preço > R$ 100.000:")
print(df.query("Zero_km == True and Valor > 100000 and Acessórios.str.contains('Freios ABS')"))

# g) liste os carros novos ou usados com km média abaixo de 10.000 km que custam até R$ 100.000
print("9.g - Carros novos ou usados com Km média < 10.000 e custo <= R$ 100.000:")
print(df.query("(Km_media < 10000) and (Valor <= 100000)"))
