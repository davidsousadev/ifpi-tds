"""

16.  Faça uma função que leia um número não determinado de valores positivos 
e retorna a média aritmética dos mesmos.

"""

def media_valores(valores):
    return sum(valores) / len(valores) if valores else 0

# Teste
assert media_valores([1, 2, 3, 4]) == 2.5
assert media_valores([5, 10, 15]) == 10
assert media_valores([]) == 0
print("Todos os testes passaram!")