"""

4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.


"""


from random import *

while True:
    try:
        lista = []
        x = (randint(1, 100))
        lista.append(x)
        maior = x
        menor = x
        for _ in range(0, 14):
            x = (randint(1, 100))
            lista.append(x)
            if x >= maior:
                maior = x
            elif x <= menor:
                menor = x
        
        for x in range(len(lista)):
            if lista[x]== maior:
                posicaoMaior = x
            elif lista[x]== menor:
                posicaoMenor = x 
            
        print("Maior número: ", maior)
        print("Posição do maior número na lista: ", posicaoMaior)
        
        print("Menor número: ", menor)
        print("Posição do menor número na lista: ", posicaoMenor)
        
        break 
    except ValueError:
        print("\n Número invalido! \n")