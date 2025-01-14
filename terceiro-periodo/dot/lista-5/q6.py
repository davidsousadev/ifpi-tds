"""

6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False


"""

def lista_ordenada(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    return lista == sorted(lista)

# Testes
assert lista_ordenada([1, 2, 3]) == True
assert lista_ordenada([0, 5, 10, 20]) == True
assert lista_ordenada([-5, -3, 0, 4]) == True
assert lista_ordenada([3, 7, 2]) == False
assert lista_ordenada([10, 5, 0]) == False
assert lista_ordenada([1, 2, 2, 1]) == False
assert lista_ordenada([0, -1, -2]) == False

assert lista_ordenada([]) == Exception
assert lista_ordenada([7]) == Exception
assert lista_ordenada("[]") == Exception
assert lista_ordenada(9696) == Exception
assert lista_ordenada(None) == Exception
assert lista_ordenada(True) == Exception
assert lista_ordenada(["7", "b", "26"]) == Exception
assert lista_ordenada([1, "2", 3, 4.0]) == Exception

print("Todos os testes passaram!")
