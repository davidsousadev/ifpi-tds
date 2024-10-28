"""1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar."""

def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


while True:
    try:
        num = int(input("Digite um número inteiro: "))
        print(f"O número {num} é :", par_ou_impar(num))
        break

    except:
        print("\nDigite um número inteiro valido!\n")