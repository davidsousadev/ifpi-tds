"""

5)  Faça  um  programa  que  leia  duas  listas  de  10  elementos  numéricos  cada  um  e  intercale  os 
elementos deste em uma outra lista de 20 elementos.

"""

from random import *

def unirListas():
    lista1 = [] 
    lista2 = []
    uniao = []
    for x in range(10):
        lista1.append(randint(0,100))
        uniao.append(lista1[x])
        lista2.append(randint(0,100))
        uniao.append(lista2[x])  
    return uniao


while True:
    try:
        uniao = unirListas()
        print(uniao)
        break 
    except ValueError:
        print("\n Número invalido! \n")
