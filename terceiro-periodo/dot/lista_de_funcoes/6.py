"""

6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

"""

def calcular_poligono(quantidade_de_lados, medida):
    if quantidade_de_lados == 3:
        perimetro = medida * 3
        return f"TRIÂNGULO: Perímetro = {perimetro} cm"
    elif quantidade_de_lados == 4:
        area = medida ** 2
        return f"QUADRADO: Área = {area} cm²"
    elif quantidade_de_lados == 5:
        return "PENTÁGONO"
    else:
        return "Número de lados inválido."

while True:
    try:
        quantidade_de_lados = int(input("Digite a quantidade de lados: 3, 4 ou 5: "))
        if quantidade_de_lados >=3 and quantidade_de_lados <= 5:
            break
        else:
            print("\nDigite uma quantidade válida!\n")
    except ValueError:
        print("\nDigite uma quantidade válida!\n")


while True:
    try:
        medida = float(input(f"Digite a medida do lado (em cm): "))
        print(calcular_poligono(quantidade_de_lados, medida))
        break
    except ValueError:
        print("\nDigite uma medida válida!\n")


