"""

12.  Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os 
ordenados em ordem crescente.

"""

def ordenar(val1, val2):
    return (min(val1, val2), max(val1, val2))

# Teste
assert ordenar(5, 3) == (3, 5)
assert ordenar(1, 10) == (1, 10)
assert ordenar(8, 8) == (8, 8)
print("Todos os testes passaram!")