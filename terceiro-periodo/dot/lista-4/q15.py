"""

15.  A  prefeitura  de  uma  cidade  fez  uma  pesquisa  entre  os  seus  habitantes, 
coletando dados sobre o salário e número de filhos. Faça uma função que leia 
esses dados para um número não determinado de pessoas e retorne a média de 
salário da população, a média do número de filhos, o maior salário e o percentual 
de pessoas com salário até R$ 350,00. 

"""

def estatisticas_populacao(salarios, filhos):
    total_salarios = sum(salarios)
    total_filhos = sum(filhos)
    maior_salario = max(salarios)
    percentual = sum(1 for s in salarios if s <= 350) / len(salarios) * 100
    return total_salarios / len(salarios), total_filhos / len(filhos), maior_salario, percentual

# Teste
salarios = [300, 500, 400, 350]
filhos = [2, 3, 1, 4]
assert estatisticas_populacao(salarios, filhos) == (387.5, 2.5, 500, 50.0)
print("Todos os testes passaram!")