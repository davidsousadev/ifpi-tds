'''
As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):

a) len(), que recebe uma lista e retorna número de itens; b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida; c) min(),que recebe uma lista e retorna o menor valor d) max(), que recebe uma lista retorna o maior valor e) sum(), que recebe uma lista retorna a soma dos valores

Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o resultado encontrado.

Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().

'''



def inserirItens(elementos):
    while True:
        valor = int(input("Digite numero inteiro / digite 0 para o loop: "))
        if valor == 0:
            break
        elementos.append(valor)
    return elementos



def comprimento(lista):
    cont = 0
    for _ in lista:
        cont += 1
    return cont



def inverter(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida



def minimo(lista):
    if lista != []:
        menor = sorted(lista)
        menor = menor[0]
        return menor
    else:
        return 0



def maximo(lista):
    maior = float()
    for num in lista:
        if num > maior:
            maior = num
    return maior



def soma(lista):
    total = 0
    for num in lista:
        total += num
    return total



def main():
    elementos = []
    elementos = inserirItens(elementos)
    print(f"Lista dos elementos: {elementos}")
    print(f"Contem {comprimento(elementos)} elementos.")
    print(f"Lista dos elementos invertidos: {inverter(elementos)}")
    print(f"Menor numero: {minimo(elementos)}")
    print(f"Maior numero: {maximo(elementos)}")
    print(f"Soma dos numeros: {soma(elementos)}")



if __name__ == '__main__':
    main()