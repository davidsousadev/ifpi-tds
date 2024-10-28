"""6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5."""

def lados(numero_de_lados, lados):
    if numero_de_lados==3:
        perimetro = 0
        for lado in lados:
            perimetro += lado
    return f"TRIÂNGULO: {perimetro}"


while True:
    try:
        quantidade_de_lados = int(input("Digite a quantidade de lados: 3 , 4 ou 5: "))
        if quantidade_de_lados >= 3 and quantidade_de_lados <= 5:
            break
    except:
        print("\nDigite uma quantidade valida!\n")


while True:
    try:
        lados = []
        for lado in range(quantidade_de_lados):
            try:
                medida = float(input(f"Digite a medida do lado {lado} (em cm): "))
                lados.append(medida)
            except:
                print("\nDigite uma medida valida!\n")
            break

    except:
        print("\nDigite uma altura valida!\n")

print(f"{lados(numero_de_lados, lados)}")