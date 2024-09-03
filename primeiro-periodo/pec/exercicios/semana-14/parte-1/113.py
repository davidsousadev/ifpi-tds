# Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.



def inserirItens():
    lista = []
    for i in range(20):
        valor = int(input("Digite um numero inteiro: "))
        lista.append(valor)
    return lista



def somaElementos(lista_a, lista_b):
    lista = []
    for i in range(20):
        lista.append(lista_a[i] + lista_b[i])
    return lista



def main():
    lista_a = inserirItens()
    lista_b = inserirItens()
    lista_c = somaElementos(lista_a, lista_b)
    print(f"Lista A:{lista_a}")
    print(f"Lista B:{lista_b}")
    print(f"Lista C soma das listas:{lista_c}")



if __name__ == '__main__':
    main()