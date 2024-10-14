"""

13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

"""

def calcula_s(n):
    return sum(1/i for i in range(1, n + 1))

while True:
    try:
        num = int(input("Digite um número inteiro positivo: "))
        print(f"O valor de S é: {calcula_s(num):.2f}")
        break 
    except ValueError:
        print("\nDigite um número inteiro positivo valido!\n")