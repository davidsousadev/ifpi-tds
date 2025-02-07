"""
    INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
    CAMPUS TERESINA CENTRAL
    TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
    PROF.: Rogerio da Silva Batista
    Alunos: David Sousa da Silva - 2023211MTDS0022
            GERSON OLIVEIRA REIS - 2023211MTDS0016  
            PEDRO AUGUSTO RODRIGUES MELO - 2023211MTDS0072
    Disciplina: Tópicos Especiais em Programação
    DATA: 07/02/2025
"""

"""

Com base nos seguintes datasets:

1. Carros
2. Titanic
3. Vinhos
4. VideoGames
5. Anac

Grupos:
Grupo 1: Carros
Gerson
David
Pedro Augusto

Calcule a matriz de correlação de Pearson e em seguida plote os gráficos
adequados para cada par de variáveis com coeficiente diferente de zero.

"""
"""
# Exemplo:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Passo 1: Carregar o Dataset
# Exemplo: carregar um dataset de carros
dados = {
'Idade': [45, 20, 25, 40, 34],
'Salário': [10000, 70000, 5000, 9000, 8000],
'Experiência': [13, 2, 5, 10, 12]
}

# Passo 2: Calcular a Matriz de Correlação
df = pd.DataFrame(dados)
matriz_correlacao = df.corr()

# Passo 3: Exibir a Matriz de Correlação
print(matriz_correlacao)

# Opcional: Visualizar a Matriz de Correlação usando um Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap da Matriz de Correlação')
plt.show()
"""

# Solução

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Função para processar um dataset
def processar_dataset(nome_arquivo, separador):
    # Carregar o dataset
    df = pd.read_csv(nome_arquivo, sep=separador)
    
    # Selecionar apenas colunas numéricas
    df_numerico = df.select_dtypes(include=['number'])

    # Remover colunas com apenas um valor único
    df_numerico = df_numerico.loc[:, df_numerico.nunique() > 1]
    
    # Verificar se há colunas numéricas
    if df_numerico.empty:
        return
    
    # Calcular a matriz de correlação de Pearson
    matriz_correlacao = df_numerico.corr(method='pearson')
    
    # Remover pares com NaN
    matriz_correlacao = matriz_correlacao.dropna(how='all').dropna(axis=1, how='all')

    # Verificar se ainda há dados após remoção de NaN
    if matriz_correlacao.empty:
        return

    # Exibir a matriz de correlação
    print(f"Matriz de Correlação - {nome_arquivo}")
    print(matriz_correlacao)
    
    # Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title(f'Heatmap da Matriz de Correlação - {nome_arquivo}')
    plt.show()

# Processar cada dataset
datasets = {
    "carros.csv": ";",
    "titanic_csv.csv": ";", # O dataset titanic_csv.csv não possui colunas numéricas relevantes.
    "drinks.csv": ";", # O dataset drinks.csv não possui colunas numéricas relevantes.
    "vgsales.csv": ",",
    # "202005.CSV": ";" # Assentos Comercializados 1.0
}

for nome, sep in datasets.items():
    processar_dataset(nome, sep)