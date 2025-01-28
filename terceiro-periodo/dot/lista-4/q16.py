"""

16.  Faça uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.

"""

def media_valores(valores):
    if type(valores) != list or len(valores) < 1:
        return Exception
    for numero in valores:
        if (type(numero) != int and type(numero) != float) or numero < 0:
            return Exception
    return sum(valores) / len(valores) if valores else 0

# Testes
assert media_valores([1, 2, 3, 4]) == 2.5
assert media_valores([5, 10, 15]) == 10
assert media_valores([100, 100.5, 10]) == 70.16666666666667
assert media_valores([10, 10, 10, 10]) == 10
assert media_valores([100, 0, 100, 100]) == 75

assert media_valores([]) == Exception
assert media_valores({10, 10, 10}) == Exception
assert media_valores(10) == Exception
assert media_valores([100, 100.5, -10]) == Exception
assert media_valores([100, 100.5, -10]) == Exception
assert media_valores(True) == Exception
assert media_valores(None) == Exception

print("Todos os testes passaram!")