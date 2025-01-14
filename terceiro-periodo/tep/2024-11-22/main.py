# Código para Gerar o Dataset
# ===========================
import numpy as np

# Gerar dados aleatórios
np.random.seed(42) # Para resultados reproduzíveis
ids = np.arange(1, 11) # IDs de 1 a 10
precos = np.random.randint(20, 200, size=10) # Preços entre R$20 e R$200
vendas_a = np.random.randint(50, 500, size=10) # Vendas na Região A
vendas_b = np.random.randint(30, 400, size=10) # Vendas na Região B
custos = np.random.randint(10, 150, size=10) # Custos entre R$10 e R$150

# Criar o dataset como um array
dataset = np.column_stack((ids, precos, vendas_a, vendas_b, custos))

# Exibir o dataset
print("Dataset de Vendas:\n", dataset)
