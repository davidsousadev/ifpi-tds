"""

9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos 
no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.  

"""

def soma_intervalo(numero1, numero2):
    return sum(range(numero1, numero2 + 1))

while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        break

    except ValueError:
        print("\nDigite um número inteiro valido!\n")


while True:
    try:
        numero2 = int(input("Digite o segundo número: "))
        if numero1 < numero2:
            print(f"A soma do intervalo é: {soma_intervalo(numero1, numero2)}")
            break
        else:
            print("n2 deve ser maior que n1. Tente novamente!")
    except ValueError:
        print("\nDigite um número inteiro valido!\n")
