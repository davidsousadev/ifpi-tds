"""

24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula 
e retorna Xz  . (sem utilizar funções ou operadores de potência prontos) 

"""

def potencia(x, z):
    result = 1
    for _ in range(z):
        result *= x
    return result

# Teste
assert potencia(2, 3) == 8
assert potencia(5, 2) == 25
assert potencia(3, 0) == 1
print("Todos os testes passaram!")