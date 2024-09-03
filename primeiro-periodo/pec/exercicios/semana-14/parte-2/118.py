# Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando elementos repetidos.
   


def inserirItens():
  lista = []
  for i in range(20):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
  return lista



def removerRepetidos(lista):
    lista2 = []
    for numero in lista:
        if numero not in lista2:
            lista2.append(numero)
    return lista2



def main():
    lista = inserirItens()
    lista2 = removerRepetidos(lista)
    print(f"Lista sem numeros repetidos : {lista2}") 
    


if __name__ == '__main__':
    main()