"""

14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + 1/1! + ½! + 1/3! + 1 /N! 

"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calcula_s_fatorial(n):
    return sum(1/fatorial(i) for i in range(n + 1))

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        print(f"O valor de S com fatoriais é: {calcula_s_fatorial(numero):.2f}")
        break 
    except ValueError:
        print("\nDigite um número inteiro positivo valido!\n")