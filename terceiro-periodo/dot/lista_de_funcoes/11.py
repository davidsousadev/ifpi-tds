"""

11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor. 

"""
def numero_de_divisores(numero):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
    return cont

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        print(f"O número de divisores de {numero} é: {numero_de_divisores(numero)}")
        break 
    except ValueError:
        print("\nDigite um número inteiro positivo valido!\n")
        
