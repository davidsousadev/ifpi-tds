"""

23.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. 
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3) 

"""

def soma_complexa(n):
    if type(n) != int or n <= 0:
        return Exception
    return sum((i**2 + 1)/(i+3) for i in range(2, n+2))

# Teste
assert soma_complexa(3) == 5.095238095238095
assert soma_complexa(5) == 12.456349206349206

assert soma_complexa(0) == Exception
assert soma_complexa(-5) == Exception
assert soma_complexa([5]) == Exception
assert soma_complexa('5') == Exception
assert soma_complexa(True) == Exception
assert soma_complexa(None) == Exception

print("Todos os testes passaram!")