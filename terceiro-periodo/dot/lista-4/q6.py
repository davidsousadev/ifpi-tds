"""

6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito 
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio. 
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar 
um valor booleano. 

"""

def numero_perfeito(num):
    if type(num) != int or num < 1:
        return Exception
    divisores = sum(i for i in range(1, num) if num % i == 0)
    return divisores == num

# Teste
assert numero_perfeito(6) == True
assert numero_perfeito(28) == True
assert numero_perfeito(12) == False
assert numero_perfeito(26561485) == False

assert numero_perfeito(12.2) == Exception
assert numero_perfeito(-12) == Exception
assert numero_perfeito("12") == Exception
assert numero_perfeito([12]) == Exception
assert numero_perfeito({12}) == Exception
assert numero_perfeito({}) == Exception
assert numero_perfeito([]) == Exception
assert numero_perfeito(True) == Exception
assert numero_perfeito(None) == Exception
print("Todos os testes passaram!")