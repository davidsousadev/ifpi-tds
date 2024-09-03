# Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2 aparece na lista.

# Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.


def inserirItens(elementos):
    while True:
        valor = int(input("Digite numero inteiro / digite 0 para o loop: "))
        if valor == 0:
            break
        elementos.append(valor)
    return elementos

def contador(lista, valor):
    cont = 0
    for elemento in lista:
        if elemento == valor:
            cont += 1
    return cont

def main():
    elementos = []
    elementos = inserirItens(elementos)
    print(f"Lista de elementos: {elementos}")
    pesquisa = int(input())
    print(f"Item pesquisado: {pesquisa}")
    print(f"Quantidade de vezes que o elemento aparece na lista: {contador(elementos, pesquisa)}")



if __name__ == '__main__':
    main()