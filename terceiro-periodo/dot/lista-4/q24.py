"""

24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula e retorna Xz. (sem utilizar funções ou operadores de potência prontos) 

"""

def potencia(x, z):
    if (type(x) != int and type(x) != float) or (type(z) != int and type(z) != float):
        return Exception
    
    if z < 0:
        result = 1 / x
        for _ in range(abs(z) - 1):
            result *= 1 / x
    else:
        result = 1
        for _ in range(z):
            result *= x
    
    return result

# Testes
assert potencia(2, 3) == 8
assert potencia(5, 2) == 25
assert potencia(3, 0) == 1
assert potencia(0, 0) == 1
assert potencia(2, -1) == 0.5
assert potencia(-5, 5) == -3125

assert potencia('5', 5) == Exception
assert potencia([5], 5) == Exception
assert potencia(True, 5) == Exception
assert potencia(None, 5) == Exception

print("Todos os testes passaram!")