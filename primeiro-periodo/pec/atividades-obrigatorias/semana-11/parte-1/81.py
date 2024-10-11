'''Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre em quantos anos o valor acumulado será o dobro do valor inicial.'''



def calcular_juros(valor, taxa):
    montante = valor
    anos = 0
    while montante < valor * 2:
        montante = montante*(1 + taxa/100)
        anos += 1
    return anos



def main():    
    valor = float(input("Digite o valor do depósito:"))
    taxa = float(input("Digite a taxa de juros ao ano de uma poupança:"))
    anos = calcular_juros(valor, taxa)
    print(f"Em {anos} anos o valor acumulado será o dobro do valor inicial.")


if __name__ == '__main__':
    main()