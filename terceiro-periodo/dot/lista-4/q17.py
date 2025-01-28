"""

17. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

"""
from random import randint
def maior_menor(valores):
    if type(valores) != list:
        return Exception
    if len(valores) != 50:
        return Exception
    for numero in valores:
        if (type(numero) != int and type(numero) != float) or numero < 0:
            return Exception
    return max(valores), min(valores)


# Teste
assert maior_menor([x for x in range(0, 50)]) == (49, 0)
assert maior_menor([x for x in range(50, 100)]) == (99, 50)


assert maior_menor([17, 49, 18, 36, 37, 1, 48, 32, 28, 19, 34, 7, 42, 42, 21, 30, 20, 22, 9, 29, 38, 21, 6, 18, 36, 34, '26', 15, 13, 23, 23, 27, 2, 30, 18, 16, 1, 35, 30, 23, 21, 24, 14, 8, 26, 32, 35, 17, 46, 1]) == Exception
assert maior_menor({17, 49, 18, 36, 37, 1, 48, 32, 28, 19, 34, 7, 42, 42, 21, 30, 20, 22, 9, 29, 38, 21, 6, 18, 36, 34, 26, 15, 13, 23, 23, 27, 2, 30, 18, 16, 1, 35, 30, 23, 21, 24, 14, 8, 26, 32, 35, 17, 46, 1}) == Exception
assert maior_menor([x for x in range(0, 100)]) == Exception
assert maior_menor([50]) == Exception
assert maior_menor(True) == Exception
assert maior_menor(None) == Exception

print("Todos os testes passaram!")