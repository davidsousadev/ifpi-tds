"""

15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3) 

"""

def calcula_s(n):
    soma = 0
    for t in range(2, n + 2):
        soma += (t**2 + 1) / (t + 3)
    return soma

while True:
    try:
        munero = int(input("Digite um número inteiro positivo: "))
        print(f"O valor de S é: {calcula_s(munero):.2f}")
        break 
    except ValueError:
        print("\nDigite um número inteiro positivo valido!\n")