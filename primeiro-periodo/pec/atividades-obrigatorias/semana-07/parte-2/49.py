'''Prazo de Entrega: 25/09/2023 12:00:00 Fechado
Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente:

Signo	Aniversário
Áries	21/03 a 19/04
Touro	20/04 a 20/05
Gêmeos	21/05 a 21/06
Câncer	22/06 a 22/07
Leão	23/07 a 22/08
Virgem	23/08 a 22/09
Libra	23/09 a 22/10
Escorpião	23/10 a 21/11
Sagitário	22/11 a 21/12
Capricórnio	22/12 a 19/01
Aquário	20/01 a 18/02
Peixes	19/02 a 20/03'''

def signos(dia, mes):
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        return "Gêmeos"
    elif (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "Virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "Aquário"
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        return "Peixes"
    else:
        return "Data invalida"

def main():
    dia = int(input("Digite o dia em que você nasceu: "))
    mes = int(input("Digite o mês em que voce nasceu: "))
    resultado = signos(dia, mes)
    print(f'Seu signo é {resultado}.')



if __name__ == '__main__':
    main()
