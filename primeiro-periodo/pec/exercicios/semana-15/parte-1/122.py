# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Desenvolva uma função que soma duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais).


def convertecelcius(temperatura):
    return ((temperatura - 32) * (5/9))

def converteFahrenheit(temperatura):
    return ((temperatura * (9/5)) + 32)

def temperaturaMaisAlta(temp1,temp2):
    valor1, escala1 = temp1
    valor2, escala2 = temp2
 
    if (escala1 != escala2):
        if (escala1 == "F"):
            valor1 = convertecelcius(valor1)
            escala1 = "C"
        else:
            valor1 = converteFahrenheit(valor1)
            escala1 = "F"

    return round(valor1 + valor2, 4), escala2


def main():
    temp1 = float(input("Digite a primeira temperatura: "))
    escala1 = str(input("Digite a primeira escala: ").upper()[0])
    temp2 = float(input("Digite a segunda temperatura: "))
    escala2 = str(input("Digite a segunda escala: ").upper()[0])

    tupla = temperaturaMaisAlta((temp1, escala1), (temp2, escala2))

    print (f"Essa e a soma das temperaturas {tupla[0]} e a escala {tupla[1]}")
    
if __name__ == "__main__":
    main()