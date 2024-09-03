def ordenar(n1, n2, n3):
    #maior, medio, menor = 0
    if (n1 >= n2 and n1 >= n3):
        maior = n1
    elif(n2 >= n3):
        maior = n2
    else:
        maior = n3


    if (n2 >= n1 and n3 >= n1):
        menor = n1
    elif (n3 >= n2):
        menor = n2
    else:
        menor = n3

    if (maior != n1 and menor != n1):
        medio = n1
    if (maior != n2 and menor != n2):
        medio = n2
    if (maior != n3 and menor != n3):
        medio = n3
    return menor, medio, maior



def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    o1, o2, o3 = ordenar(n1, n2, n3)

    print(f'Essa e a ordem crescente dos números {o1}, {o2}, {o3}')

if __name__ == '__main__':
    main()
