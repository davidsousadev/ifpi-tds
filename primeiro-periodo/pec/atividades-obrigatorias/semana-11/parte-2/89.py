'''
O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.

CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5.50
C       Cheeseburger    6.80
M       Misto Quente    4.50
A       Americano       7.00
Q       Queijo Prato    4.00
X       PARA TOTAL DA CONTA
Escreva um programa que leia o código e a quantidade de cada item comprado por um freguês, calcule e exiba o total a pagar. Obs: A leitura do código 'X' indica o fim dos itens.'''

def calcular_a_conta(codigo, total):
    if codigo == 'H':
        total += 5.50
    elif codigo == 'C':
        total += 6.80
    elif codigo == 'M':
        total += 4.50
    elif codigo == 'A':
        total += 7.00
    elif codigo == 'Q':
        total += 4.00
    elif codigo == 'X':
        print(f"{total:.2f}")
    else:
        print('Opção inválida.')
    return total



def main():
    print("O programa exibe o cardápio de uma casa de lanches, especializada em sanduíches")
    total = 0
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")
        codigo = input().upper()[0]
        total = calcular_a_conta(codigo, total)
        if codigo == 'X':
            break


if __name__ == '__main__':
    main()