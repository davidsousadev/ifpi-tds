"""

5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
[1,3,6]


"""

def soma_cumulativa(lista):
    if type(lista) != list:
        return Exception
    if len(lista) == 0 or len(lista) == 1:
        return Exception
    for item in lista:
        if type(item) != int:
            return Exception

    soma = 0
    resultado = []
    for num in lista:
        soma += num
        resultado.append(soma)
    return resultado

# Testes
assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]
assert soma_cumulativa([0, 0, 0]) == [0, 0, 0]
assert soma_cumulativa([10, -10, 5]) == [10, 0, 5]
assert soma_cumulativa([-1, -2, -3]) == [-1, -3, -6]
assert soma_cumulativa([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]

assert soma_cumulativa([]) == Exception 
assert soma_cumulativa([5]) == Exception
assert soma_cumulativa("[]") == Exception
assert soma_cumulativa(777) == Exception
assert soma_cumulativa(None) == Exception
assert soma_cumulativa(True) == Exception
assert soma_cumulativa(["a", "b", "c"]) == Exception
assert soma_cumulativa([1, "b", 3]) == Exception

print("Todos os testes passaram!")
