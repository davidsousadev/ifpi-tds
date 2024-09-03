# Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ... ).


def converter_para_kelvin(temperatura, escala):
    if escala == 'C':
        return temperatura + 273.15
    elif escala == 'F':
        return round(((temperatura - 32) * 5/9 + 273.15), 2)
    elif escala == 'K':
        return temperatura
    
def calculoDeTemperaturas():
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
    temperaturas = []
    for i in range(12):
        temperatura = float(input(f"Digite a temperatura {i+1}: "))
        escala = str(input(f"Digite a escala {i+1}: ").strip())
        temperatura_kelvin = converter_para_kelvin(round(temperatura, 2), escala.upper())
        temperaturas.append(temperatura_kelvin)    
    media_anual_kelvin = round ((sum(temperaturas) / len(temperaturas)), 2)
    return media_anual_kelvin, temperaturas, meses
       
def main():
    media_anual_kelvin, temperaturas, meses = calculoDeTemperaturas()
    print("TEMPERATURA MÉDIA ANUAL")
    print(f"{round(media_anual_kelvin, 2)}K")
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    for i in range(12):
        if temperaturas[i] > media_anual_kelvin:
            print(f"{meses[i]}: {round(temperaturas[i], 2)}K")

if __name__ == "__main__":
    main()
