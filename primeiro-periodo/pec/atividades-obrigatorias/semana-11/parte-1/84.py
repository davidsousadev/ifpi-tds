'''Escreva um programa que leia número inteiro qualquer e mostre na forma invertida.'''



def numero_inverso(num):
    inverso = 0
    while num > 0:
        d = num % 10
        inverso = inverso * 10 + d
        num //= 10
    return inverso



def main():
    num = int(input("Escreva um número inteiro positivo: "))
    inverso = numero_inverso(num)
    print(f"Esse e o numero inverso: {inverso}")




if __name__ == '__main__':
	main()