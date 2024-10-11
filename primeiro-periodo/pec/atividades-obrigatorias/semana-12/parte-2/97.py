'''A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.
'''



def calculoFibonacci(numero):
    fibonacci = 0
    print(f"{fibonacci}", end="")
    fibonacci = 1
    termoA = 0
    termoB = 1
    termo = 0
    while fibonacci < numero:
        termo = termoA + termoB
        termoB = termoA
        termoA = termo 
        fibonacci += 1  
        print(f", {termo}", end="")



def main():
    numero = int(input("Digite um número de termos para a sequência de fibonacci: "))
    fibonacci = calculoFibonacci(numero)




if __name__ == '__main__':
    main()