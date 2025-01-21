"""

15.  A  prefeitura  de  uma  cidade  fez  uma  pesquisa  entre  os  seus  habitantes, 
coletando dados sobre o salário e número de filhos. Faça uma função que leia 
esses dados para um número não determinado de pessoas e retorne a média de 
salário da população, a média do número de filhos, o maior salário e o percentual 
de pessoas com salário até R$ 350,00. 

"""

def estatisticas_populacao(salarios, filhos):
    if (type(salarios)!=list or type(filhos)!=list):
        return Exception
    
    if (len(salarios)==0 or len(filhos)==0):
        return Exception
    
    if (len(salarios)!=len(filhos)):
        return Exception
    
    for filho in filhos:
        if type(filho)!=int or 0 <= filho >= 20:
            return Exception
        
    for salario in salarios:
        if type(salario)!=float or salario<=0:
            return Exception 
           
    total_salarios = sum(salarios)
    total_filhos = sum(filhos)
    maior_salario = max(salarios)
    percentual = sum(1 for salario in salarios if salario <= 350) / len(salarios) * 100
    return total_salarios / len(salarios), total_filhos / len(filhos), maior_salario, percentual

# Testes
assert estatisticas_populacao([300.00, 500.00, 400.00, 350.00], [2, 3, 1, 4]) == (387.5, 2.5, 500, 50.0)
assert estatisticas_populacao([1.00, 1.00, 1.00, 1.00], [1, 1, 1, 1]) == (1.0, 1.0, 1.0, 100.0)

assert estatisticas_populacao([00.00, 00.00, 00.00, 00.00], [0, 0, 0, 0]) == Exception
assert estatisticas_populacao([300.00, 500.00, 400.00, 350], [2, 3, 1, 4]) == Exception
assert estatisticas_populacao([300.00, 500.00, 400.00, 350.00], ["2", 3, 1, 4]) == Exception
assert estatisticas_populacao([], []) == Exception
assert estatisticas_populacao("", "") == Exception
assert estatisticas_populacao(True, True) == Exception
assert estatisticas_populacao(None, None) == Exception

print("Todos os testes passaram!")