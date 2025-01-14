from main import *
from tarefa3 import dataset_com_receita
# 4. Visualização de Insights
# Ordenar o dataset pela "Receita Total" (ordem decrescente)
dataset_ordenado = dataset_com_receita[dataset_com_receita[:, -1].argsort()[::-1]]

print("Dataset ordenado pela receita total (decrescente):\n", dataset_ordenado)

# Calcular o volume total de vendas
volume_total_a = np.sum(dataset[:, 2])  # Vendas Região A
volume_total_b = np.sum(dataset[:, 3])  # Vendas Região B

# Encontrar a região com maior volume de vendas
if volume_total_a > volume_total_b:
    print(f"A Região A tem maior volume de vendas: {volume_total_a} unidades.")
else:
    print(f"A Região B tem maior volume de vendas: {volume_total_b} unidades.")