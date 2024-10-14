"""

12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor. 

"""

def somatorio(n):
    return sum(range(1, n + 1))

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        print(f"O somatório de {numero} é: {somatorio(numero)}")
        break
    except ValueError:
        print("\nDigite um número inteiro positivo valido!\n")