"""

2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;

"""

PI = 3.14159265359

def calcular_area(raio):
    return PI * raio ** 2
    
def calcular_perimetro(raio):
    return PI * 2 * raio


while True:
    try:
        raio = int(input("Digite o raio do circulo: "))
        print(f"Área do circulo para um raio de {raio} é :", calcular_area(raio))
        print(f"Perímetro do circulo para o raio de {raio} é :", calcular_perimetro(raio))
        break

    except ValueError:
        print("\nDigite um raio valido!\n")