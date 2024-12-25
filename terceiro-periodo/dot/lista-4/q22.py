import math
def soma_fatorial_inverso(n):
    return sum(1/math.factorial(i) for i in range(1, n+1))

# Teste
assert soma_fatorial_inverso(3) == 1 + 1/1 + 1/2
assert soma_fatorial_inverso(4) == 1 + 1/1 + 1/2 + 1/6
assert soma_fatorial_inverso(1) == 1
print("Todos os testes passaram!")