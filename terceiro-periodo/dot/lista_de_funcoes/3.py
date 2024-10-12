"""3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5"""

def celcius(temperatura_fahrenheit):
    return (((temperatura_fahrenheit-32)/9)*5)

while True:
    try:
        temperatura_fahrenheit = float(input("Digite a tamperatura em Fahrenheit: "))
        print(f"A temperatura {temperatura_fahrenheit}°F é {(celcius(temperatura_fahrenheit)):.2f}°C")
        break

    except:
        print("\nDigite uma temperatura valida!\n")