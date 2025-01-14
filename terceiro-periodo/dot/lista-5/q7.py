"""

7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False


"""

def verifica_duplicados(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    return len(lista) != len(set(lista))


# Testes

assert verifica_duplicados([1, 2, 3, 1]) == True
assert verifica_duplicados([5, 5, 5, 5]) == True
assert verifica_duplicados([10, -10, 0, 10]) == True
assert verifica_duplicados([0, 0]) == True
assert verifica_duplicados([3, 7, 2, 4]) == False
assert verifica_duplicados([-5, -3, 0, 4]) == False

assert verifica_duplicados([]) == Exception
assert verifica_duplicados([1]) == Exception
assert verifica_duplicados("[]") == Exception
assert verifica_duplicados(7474) == Exception
assert verifica_duplicados(None) == Exception
assert verifica_duplicados(True) == Exception
assert verifica_duplicados(["1", 0, "3"]) == Exception
assert verifica_duplicados([-3, "b", 3]) == Exception

print("Todos os testes passaram!")
