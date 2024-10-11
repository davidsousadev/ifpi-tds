'''

01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
ímpar. Mostre na tela o resultado da operação.

'''


def somarNumero(numero):
    if numero % 2 == 0:
        numero += 5
    else:
        numero += 8
    return numero



def main():
    numero = int(input("Digite um múmero inteiro: "))
    numero = somarNumero(numero)
    print(f"Esse e o resultado da operação {numero}.")



if __name__ == '__main__':
    main()