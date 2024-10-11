'''Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.'''


def comprarAvista(valorCarro):
    poupanca = 10000
    contadorMeses = 0
    while valorCarro > poupanca:
        poupanca = poupanca + (poupanca/100) * 0.7 
        valorCarro = valorCarro + (valorCarro/100) * 0.4
        contadorMeses += 1 
    return contadorMeses


def main():
    valorCarro = int(input("Digite o valor do carro: "))
    contadorMeses = comprarAvista(valorCarro)
    print(f"Com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista em {contadorMeses} meses.")



if __name__ == '__main__':
    main()