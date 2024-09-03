# Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas
def listaParesImpares(lista,pares,impares):
    for i in range(20):
        num = int(input("Digite um valor: "))
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return lista, pares, impares


def main():
    lista = []
    pares = []
    impares = []
    n, pares, impares = listaParesImpares(lista,pares,impares)
    print(f"Lista: {lista}")
    print(f"Lista pares: {pares}")
    print(f"Lista impares: {impares}")



if __name__ == "__main__":
    main()