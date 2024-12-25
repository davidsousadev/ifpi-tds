"""

22.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N 
e retorna o valor de S. 
S = 1 + 1/1! + ½! + 1/3! + 1 /N! 

"""

import math

def soma_fatorial_inverso(n):
    return round(sum(1/math.factorial(i) for i in range(1, n+1)), 2)
# Teste
assert soma_fatorial_inverso(3) == 1.67
assert soma_fatorial_inverso(4) == 1.71
assert soma_fatorial_inverso(1) == 1.0
print("Todos os testes passaram!")