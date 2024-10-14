"""

4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).

"""

def media(nota1, nota2):
    if((nota1+nota2/2)>=6.0):
        return "PARABÉNS! Você foi aprovado!"
    else:
        return "TENTE NOVAMENTE! Você foi reprovado!"

while True:
    try:
        nota1 = float(input("Digite a primeira nota do aluno: "))
        break

    except ValueError:
        print("\nDigite uma nota valida!\n")


while True:
    try:
        nota2 = float(input("Digite a segunda nota do aluno: "))
        print(f"A sua situação com notas: {nota1} e {nota2} é: ", media(nota1, nota2))
        break
    except ValueError:
        print("\nDigite uma nota valida!\n")

