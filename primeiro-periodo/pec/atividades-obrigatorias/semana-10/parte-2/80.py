'''Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24. O programa estará correto se o usuário informar o valor 1000 e o programa produzir o seguinte resultado: 1x de R$ 1000.00 2x de R$ 500.00 3x de R$ 333.33 4x de R$ 250.00 5x de R$ 200.00 6x de R$ 166.67 7x de R$ 142.86 8x de R$ 125.00 9x de R$ 111.11 10x de R$ 100.00 11x de R$ 90.91 12x de R$ 83.33 13x de R$ 76.92 14x de R$ 71.43 15x de R$ 66.67 16x de R$ 62.50 17x de R$ 58.82 18x de R$ 55.56 19x de R$ 52.63 20x de R$ 50.00 21x de R$ 47.62 22x de R$ 45.45 23x de R$ 43.48 24  '''



def parcelamento(valor):
    for i in range(1, 25):
        parcela = valor / i
        parcela = round(parcela, 2)
        print(f'{i}x de R$ ' '%.2f'%parcela)    
    



def main():
    valor = float(input())
    valor = parcelamento(valor)



if __name__ == '__main__':
    main()