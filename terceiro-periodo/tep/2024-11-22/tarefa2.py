from main import *
# 2. Cálculos Estatísticos
# Calcule a média, mediana e desvio padrão das vendas em cada região.
media_vendas_a = np.mean(dataset[:, 2]) 
mediana_vendas_a = np.median(dataset[:, 2])
desvio_padrao_vendas_a = np.std(dataset[:, 2])

media_vendas_b = np.mean(dataset[:, 3]) 
mediana_vendas_b = np.median(dataset[:, 3])
desvio_padrao_vendas_b = np.std(dataset[:, 3])

print("Estatísticas Região A:")
print(f"Média: {media_vendas_a}, Mediana: {mediana_vendas_a}, Desvio Padrão: {desvio_padrao_vendas_a}")

print("Estatísticas Região B:")
print(f"Média: {media_vendas_b}, Mediana: {mediana_vendas_b}, Desvio Padrão: {desvio_padrao_vendas_b}")

# Determine a receita total de vendas para cada região (preço × quantidade vendida).
receita_a = dataset[:, 1] * dataset[:, 2]  
receita_b = dataset[:, 1] * dataset[:, 3]  

print("Receita Região A:", receita_a)
print("Receita Região B:", receita_b)

# Identifique o produto com maior margem de lucro (Preço - Custo).
margem_lucro = dataset[:, 1] - dataset[:, 4] 
produto_maior_margem = np.argmax(margem_lucro) 

print("Produto com maior margem de lucro:", dataset[produto_maior_margem])
