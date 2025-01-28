"""

20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

"""

def somatorio(n):
    if type(n) != int or n <= 0:
        return Exception
    return sum(range(1, n+1))

# Testes
assert somatorio(5) == 15
assert somatorio(10) == 55

assert somatorio(0) == Exception
assert somatorio(-5) == Exception
assert somatorio([5]) == Exception
assert somatorio('5') == Exception
assert somatorio(True) == Exception
assert somatorio(None) == Exception

print("Todos os testes passaram!")