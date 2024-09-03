'''Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1'''



def calculoFatorial(numero):
    fatorial = 1
    if numero!=1:
        while numero > 0:
            fatorial *= numero
            numero -= 1
    return fatorial



def main():
    numero = int(input("Digite um número: "))
    fatorial = calculoFatorial(numero)
    print(f"O valor vatorial do número {numero} é {fatorial}.")




if __name__ == '__main__':
    main()