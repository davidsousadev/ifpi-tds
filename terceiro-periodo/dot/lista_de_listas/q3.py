"""

3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da 
leitura.

"""


from random import *

while True:
    
    lista = []
    print("Digite um número inteiro, digite 0 para sair!")
    while True:
        try:
            num = int(input("Digite um número: "))
            if num !=0:
                lista.append(num)
            else:
                break
        except ValueError:
            print("\nDigite um número inteiro valido!\n")
    print(lista[::-1])
    break 
    