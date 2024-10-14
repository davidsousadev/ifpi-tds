"""

5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima)

"""


def peso_ideal(sexo, h):
    if sexo==1:
        return (62.1 * h) - 44.7
    else:
        return (72.7 * h) - 58


while True:
    try:
        sexo = int(input("Digite seu sexo: 1 = Feminino, 2 = Masculino: "))
        if sexo == 1 or sexo == 2:
            break
    except ValueError:
        print("\nDigite um sexo valido!\n")


while True:
    try:
        altura = float(input("Digite sua altura: "))
        if altura > 0 and altura <= 3:
            print(f"Seu peso ideal é: {peso_ideal(sexo, altura):.2f}")
            break
    except ValueError:
        print("\nDigite uma altura valida!\n")