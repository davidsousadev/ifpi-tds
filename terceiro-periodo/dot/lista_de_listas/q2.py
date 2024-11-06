"""

2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade 
de números negativos e a soma dos números positivos dessa lista.

"""


from random import *


while True:
    try:
        lista = []
        positivos = 0
        negativos = 0
        for _ in range(0, 10):
            x = (randrange(-10, 10))
            lista.append(x)
            if x > 0:
                positivos += 1
            elif x < 0:
                negativos += 1
        print(lista)

        print("Quantidade de números positivos: ", positivos)
        
        print("Quantidade de números negativos: ", negativos)
        
        break 
    except ValueError:
        print("\n Número invalido! \n")