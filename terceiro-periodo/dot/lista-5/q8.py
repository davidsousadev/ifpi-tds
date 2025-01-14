"""

8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5


"""

def valor_proximo_da_media(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int and type(item) != float:
            return Exception

    media = sum(lista) / len(lista)
    proximo = lista[0]
    menor_diferenca = abs(media - proximo)
    #print(menor_diferenca)
    for item in lista[1:]:
        diferenca = abs(media - item)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            proximo = item
    return proximo

# Testes
assert valor_proximo_da_media([2.5, 7.5, 10.0, 4.0]) == 7.5
assert valor_proximo_da_media([1, 2, 3, 4, 5]) == 3
assert valor_proximo_da_media([10, 20, 30, 40, 50]) == 30
assert valor_proximo_da_media([1, 10, 15, 20, 25]) == 15
assert valor_proximo_da_media([0, 100, 200, 300, 400]) == 200
assert valor_proximo_da_media([-10, -20, -30, -40, -50]) == -30
assert valor_proximo_da_media([-1, 0, 1]) == 0

assert valor_proximo_da_media([]) == Exception
assert valor_proximo_da_media("[]") == Exception
assert valor_proximo_da_media(7575) == Exception
assert valor_proximo_da_media([5]) == Exception
assert valor_proximo_da_media([-10]) == Exception
assert valor_proximo_da_media(None) == Exception
assert valor_proximo_da_media(True) == Exception
assert valor_proximo_da_media(["-1", "A"]) == Exception
assert valor_proximo_da_media([11, "b", 3]) == Exception


print("Todos os testes passaram!")
