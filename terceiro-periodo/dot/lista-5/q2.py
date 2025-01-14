"""

2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência.

"""

def contar_ocorrencias(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception
    
    ocorrencias = {}
    for num in lista:
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1
    
    return ocorrencias

# Testes
assert contar_ocorrencias([5, 4, 5, 7, 3, 4]) == {5: 2, 4: 2, 7: 1, 3: 1}
assert contar_ocorrencias([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

assert contar_ocorrencias([42]) == {42: 1}
assert contar_ocorrencias([-1, -2, -1, -3, -2]) == {-1: 2, -2: 2, -3: 1}
assert contar_ocorrencias([0, 0, 1, 0, 2]) == {0: 3, 1: 1, 2: 1}

assert contar_ocorrencias([]) == Exception
assert contar_ocorrencias("[]") == Exception
assert contar_ocorrencias(7777777) == Exception
assert contar_ocorrencias(None) == Exception
assert contar_ocorrencias(True) == Exception
assert contar_ocorrencias(["a", "b", "c"]) == Exception
assert contar_ocorrencias([0, "b", 3]) == Exception

print("Todos os testes passaram!")
