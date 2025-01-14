"""

3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25


"""

def maior_soma_segmento(lista):
    if type(lista) != list:
        return Exception
    if len(lista) < 2:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    maior_soma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        soma_atual = lista[i] + lista[i + 1]
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma

# Testes
assert maior_soma_segmento([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25
assert maior_soma_segmento([1, 2, 3, 4, 5]) == 9
assert maior_soma_segmento([-10, -20, -5, -1]) == -6
assert maior_soma_segmento([0, 0, 0, 0]) == 0
assert maior_soma_segmento([10, 20]) == 30


assert maior_soma_segmento("[0, 0, 0, 0]") == Exception
assert maior_soma_segmento(77777) == Exception
assert maior_soma_segmento([1]) == Exception
assert maior_soma_segmento(None) == Exception
assert maior_soma_segmento(True) == Exception
assert maior_soma_segmento(["a", "c"]) == Exception
assert maior_soma_segmento(["2", 7]) == Exception

print(" Todos os testes passaram!")
