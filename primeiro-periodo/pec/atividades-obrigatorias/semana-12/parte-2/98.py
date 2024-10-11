'''Calcular H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido.'''



def calcular(numero):
    h = 0
    contador = 1
    numero += 1
    while True:
        if contador < numero:
            h += 1 / contador
            contador += 1
        else:
            return round(h, 4)
            break



def main():
    numero = int(input("Digite um numero: "))
    h = calcular(numero)
    print(f"Esse e o resultado da operação com 4 casas decimais {h:.4f}.")



if __name__ == '__main__':
    main()