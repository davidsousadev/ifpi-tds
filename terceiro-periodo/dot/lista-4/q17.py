"""

17. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

"""
from random import randint
def maior_menor(valores):
    if len(valores) != 50:
        return Exception
    return max(valores), min(valores)

print([x for x in range(0, 50)])
# Teste
# assert maior_menor([x for x in range((0, 50))]) == (50, 0)
# # assert maior_menor([50, 30, 20]) == (50, 20)
# assert maior_menor([1]) == Exception
# print("Todos os testes passaram!")

