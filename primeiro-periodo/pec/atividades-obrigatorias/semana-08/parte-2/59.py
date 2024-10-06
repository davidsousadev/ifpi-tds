'''
04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para homens e 2 para mulheres.
Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
• para homens: (72.7 * altura) – 58
• para mulheres: (62.1 * altura) – 44.7
'''


def calculaPeso(altura, sexo):
    if sexo == 1:
        pesoIdeal = (72.7 * altura) - 58
    elif sexo == 2:
        pesoIdeal = (62.1 * altura) - 44.7
    return pesoIdeal



def main():
    altura = float(input("Digite a altura: "))
    sexo = int(input("Digite o sexo sendo 1 para homens e 2 para mulheres: "))

    pesoIdeal = calculaPeso(altura, sexo)
    if pesoIdeal:
        print(f'Esse e o peso ideal: ''%.2f'%pesoIdeal)


if __name__ == '__main__':
    main()