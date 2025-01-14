"""

10)Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
10, 3, 1] = 20


"""

def maior_soma_repetidos(lista):
    if type(lista) != list:
        return Exception
    if len(lista) <= 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    contagem_de_ocorrencias = {}
    for item in lista:
        if item in contagem_de_ocorrencias:
            contagem_de_ocorrencias[item] += 1
        else:
            contagem_de_ocorrencias[item] = 1
    #print(contagem_de_ocorrencias.items())
    soma_maxima = 0
    for item, count in contagem_de_ocorrencias.items():
        if count > 1:
            soma_item = item * count
            soma_maxima = max(soma_maxima, soma_item)
    #print(soma_maxima)        
    return soma_maxima


# Testes
assert maior_soma_repetidos([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert maior_soma_repetidos([1, 2, 3, 4, 5, 5, 6, 6, 6]) == 18
assert maior_soma_repetidos([10, -10, 0, 10]) == 20
assert maior_soma_repetidos([1, 2, 3, 4, 5]) == 0
assert maior_soma_repetidos([1, 1, 1]) == 3

assert maior_soma_repetidos([]) == Exception
assert maior_soma_repetidos([1]) == Exception
assert maior_soma_repetidos("[]") == Exception
assert maior_soma_repetidos(777) == Exception
assert maior_soma_repetidos(None) == Exception
assert maior_soma_repetidos(True) == Exception
assert maior_soma_repetidos([5, "b", 5]) == Exception
assert maior_soma_repetidos([1, 2, 1.5]) == Exception

print("Todos os testes passaram!")
