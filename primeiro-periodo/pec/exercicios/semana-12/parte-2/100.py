'''Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

'''


def numeroPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def imprimePrimos(x, y):
    for n in range(x, y + 1):
        if numeroPrimo(n):
            print(f"{n}")



def main():
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    imprime = imprimePrimos(x, y)
    


            
if __name__ == "__main__":
    main()