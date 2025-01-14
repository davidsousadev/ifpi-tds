from main import *
# 1. Exploração de Dados
# Imprima o formato do array (número de linhas e colunas).
print("Formato do array:", dataset.shape)

# Verifique o tipo dos dados no array.
print("Tipo dos dados no dataset:", dataset.dtype)

# Encontre o valor mínimo e máximo de cada coluna.
min_vals = dataset.min(axis=0)
max_vals = dataset.max(axis=0)

print("Valores mínimos por coluna:", min_vals)
print("Valores máximos por coluna:", max_vals)