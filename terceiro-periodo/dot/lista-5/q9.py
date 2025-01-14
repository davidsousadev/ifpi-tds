"""

9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
[7, 3]


"""

def eliminar_repetidos(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    
    contagem = {item: lista.count(item) for item in lista}
    return [item for item in lista if contagem[item] == 1]

# Testes
assert eliminar_repetidos([5, 4, 5, 7, 3, 4]) == [7, 3]
assert eliminar_repetidos([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert eliminar_repetidos([10, -10, 0, 10]) == [-10, 0]
assert eliminar_repetidos([5, 5, 5, 5]) == []

assert eliminar_repetidos([5]) == Exception
assert eliminar_repetidos("[]") == Exception
assert eliminar_repetidos(77) == Exception
assert eliminar_repetidos(None) == Exception
assert eliminar_repetidos(True) == Exception
assert eliminar_repetidos(["3", 3]) == Exception
assert eliminar_repetidos([1, 2, 3, 1.5, 2 , 4]) == Exception
assert eliminar_repetidos([]) == Exception

print("Todos os testes passaram!")
