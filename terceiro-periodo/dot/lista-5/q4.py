"""

4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34


"""

def maior_soma_segmento_qualquer(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    maximo_atual = maximo_global = lista[0]
    for i in range(1, len(lista)):
        maximo_atual = max(lista[i], maximo_atual + lista[i])
        if maximo_atual > maximo_global:
            maximo_global = maximo_atual

    return maximo_global

# Testes
assert maior_soma_segmento_qualquer([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
assert maior_soma_segmento_qualquer([1, 2, 3, 4, 5]) == 15
assert maior_soma_segmento_qualquer([-1, -2, -3, -4]) == -1
assert maior_soma_segmento_qualquer([10, -1, 20, -2, 30, -3]) == 57
assert maior_soma_segmento_qualquer([0, 0, 0, 0]) == 0


assert maior_soma_segmento_qualquer("[]") == Exception
assert maior_soma_segmento_qualquer(77777) == Exception
assert maior_soma_segmento_qualquer([]) == Exception
assert maior_soma_segmento_qualquer(None) == Exception
assert maior_soma_segmento_qualquer(True) == Exception
assert maior_soma_segmento_qualquer(["a", "b"]) == Exception
assert maior_soma_segmento_qualquer([1, "1"]) == Exception

print("Todos os testes passaram!")

