"""

1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"O número {numero} é : {par_ou_impar(numero)}")
        break
    except ValueError:
        print("\nDigite um número inteiro valido!\n")