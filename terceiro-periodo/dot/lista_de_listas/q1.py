"""

1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.

"""
from random import randint

def calculaPares(lista):
    pares = 0
    lista_pares = []
    for x in lista:
        if x % 2==0:
            pares += 1
            lista_pares.append(x)
    return pares, lista_pares

def calculaImpares(lista):
    impares = 0
    lista_impares = []
    for x in lista:
        if x % 2!=0:
            impares += 1
            lista_impares.append(x)
    return impares, lista_impares

while True:
    try:
        lista = []
        for x in range(0, 100):
            lista.append(randint(0, 100))

        pares, lista_pares = calculaPares(lista)
        print("Quantidade de números pares: ", pares, lista_pares)
        impares, lista_impares = calculaImpares(lista)
        print("Quantidade de números impares: ", impares, lista_impares)
        break 
    except ValueError:
        print("\n Número invalido! \n")