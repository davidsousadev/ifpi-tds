"""

1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]


"""


def remove_repeticoes_de_lista(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception
    return list(dict.fromkeys(lista))


# Testes

assert remove_repeticoes_de_lista([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
assert remove_repeticoes_de_lista([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_repeticoes_de_lista([1, 1, 1, 1, 1]) == [1]
assert remove_repeticoes_de_lista([-1, -2, -1, -3, -2]) == [-1, -2, -3]
assert remove_repeticoes_de_lista([0, 0, 1, 0, 2]) == [0, 1, 2]

assert remove_repeticoes_de_lista([]) == Exception
assert remove_repeticoes_de_lista([42]) == Exception
assert remove_repeticoes_de_lista("[]") == Exception
assert remove_repeticoes_de_lista(7777777) == Exception
assert remove_repeticoes_de_lista(None) == Exception
assert remove_repeticoes_de_lista(True) == Exception
assert remove_repeticoes_de_lista(["a", "b", "c"]) == Exception
assert remove_repeticoes_de_lista([1, "1", 2]) == Exception

print("Todos os testes passaram!")
