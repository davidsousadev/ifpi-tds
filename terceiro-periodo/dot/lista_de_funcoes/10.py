"""

10. Escreva um programa composto de uma função Max e o programa principal como segue:  
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer u m deles;  
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função 
Max.

"""

def max(numero1, numero2):
    return numero1 if numero1 > numero2 else numero2

while True:
    try:
        print("Digite dois números e descubra qual é o maior!")
        for x in range(4):
            print(f"Essa é a série {x+1}.")
            while True:
                try:
                    numero1 = int(input("Digite o primeiro número: "))
                    break
                except ValueError:
                    print("\nDigite um número inteiro valido!\n")
            while True:
                try:     
                    numero2 = int(input("Digite o segundo número: "))
                    print(f"O maior número é: {max(numero1, numero2)}")
                    break
                except ValueError:
                    print("\nDigite um número inteiro valido!\n")
        break 
    except ValueError:
        print("\nDigite um número inteiro valido!\n")

