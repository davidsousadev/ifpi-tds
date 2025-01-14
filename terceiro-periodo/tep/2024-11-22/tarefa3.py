from main import *
from tarefa2 import receita_a, receita_b

# 3. Manipulação de Dados
# Adicionar coluna de "Receita Total"
receita_total = receita_a + receita_b
dataset_com_receita = np.column_stack((dataset, receita_total))

print("Dataset com a nova coluna 'Receita Total':\n", dataset_com_receita)

# Filtrar produtos com receita total acima de R$10.000
produtos_acima_10000 = dataset_com_receita[dataset_com_receita[:, -1] > 10000]

print("Produtos com receita total acima de R$10.000:\n", produtos_acima_10000)