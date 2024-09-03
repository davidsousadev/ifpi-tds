# Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

def intercalarListas(lista_a, lista_b, lista_c):
    for x in range(25):
        lista_c.append(lista_a[x])
        lista_c.append(lista_b[x])
    return lista_c


def preencherLista_a(lista_a):
    for i in range(25):
        valor = int(input("Digite os elementos da lista A: "))
        lista_a.append(valor)
    return lista_a

def preencherLista_b(lista_b):
    for i in range(25):
        valor = int(input("Digite os elementos da lista B: "))
        lista_b.append(valor)
    return lista_b


def main():
    lista_a = []
    lista_b = []
    lista_c = []
    lista_a = preencherLista_a(lista_a)
    lista_b = preencherLista_b(lista_b)
    lista_c = intercalarListas(lista_a, lista_b, lista_c)

    print(f"Lista A: {lista_b}")
    print(f"Lista B: {lista_a}")
    print(f"Uniao das listas : {lista_c}")

if __name__ == "__main__":
    main()
