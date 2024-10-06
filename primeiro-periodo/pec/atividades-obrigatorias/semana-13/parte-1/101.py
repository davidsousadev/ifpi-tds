'''
Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.'''
def lista_10(lista, soma, multiplicacao):

    for x in range(10):
        n = int(input())
        lista[x] = n
        soma += n
        multiplicacao *= n
    
    return lista, soma, multiplicacao
    
    
def main():
    lista = [0,0,0,0,0,0,0,0,0,0]
    soma = 0
    multiplicacao = 1
    lista, soma, multiplicacao = lista_10(lista, soma, multiplicacao)
    print(f"Essa é a lista: {lista}")
    print(f"Essa é a soma: {soma}")
    print(f"Essa é a Multiplicação: {multiplicacao}")




if __name__ == '__main__':
    main()