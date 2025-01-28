"""

21.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. 
S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

"""

def soma_fracoes(n):
    if type(n) != int or n <= 0:
        return Exception
    return sum(1/i for i in range(1, n+1))

# Testes
assert soma_fracoes(3) == 1 + 1/2 + 1/3
assert soma_fracoes(5) == 1 + 1/2 + 1/3 + 1/4 + 1/5
assert soma_fracoes(1) == 1

assert soma_fracoes(0) == Exception
assert soma_fracoes(-5) == Exception
assert soma_fracoes([5]) == Exception
assert soma_fracoes('5') == Exception
assert soma_fracoes(True) == Exception
assert soma_fracoes(None) == Exception

print("Todos os testes passaram!")