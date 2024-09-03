#Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior
#elemento e a posição que ele se encontra.

# Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a posição que ele se encontra.

# Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a posição que ele se encontra.

def maiorElemento(lista):
    maior = lista[0]
    posicao = 0
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i
    return maior, posicao



def inserirItens(lista):
  lista = []
  for x in range(10):
    num = int(input("Digite um numero: "))
    lista.append(num)
  return lista



def main():
  numeros = []
  print(f"Lista: {numeros}")
  maior_elemento, posicao_maior = maiorElemento(numeros)
  print(f"Maior elemento :{maior_elemento}")
  print(f"Posicao :{posicao_maior}")



if __name__ == '__main__':
    main()