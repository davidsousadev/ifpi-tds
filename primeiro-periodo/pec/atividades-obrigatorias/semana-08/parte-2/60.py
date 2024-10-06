'''
05. Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas
obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final =

Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios

7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito Média Final
A >= 9.0
B >= 7.5 e < 9.0
C >= 6.0 e < 7.5
D >= 4.0 e < 6.0
E < 4.0

O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado”
se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
'''



def calcularMedia(n1, n2, n3, mediaExercicio):
    media = (n1 + n2 * 2 + n3 * 3 + mediaExercicio) / 7
    if media >= 9.0:
        return media, 'A'
    elif 7.5 <= media < 9.0:
        return media, 'B'
    elif 6.0 <= media < 7.5:
        return media, 'C'
    elif 4.0 <= media < 6.0:
        return media, 'D'
    else:
        return media, 'E'



def main():
    matricula = str(input("Digite a matricula: ").strip())
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    mediaExercicio = float(input("Digite a média dos exercicios: "))

    media, conceito = calcularMedia(n1, n2, n3, mediaExercicio)

    print(f'Essa é a matricula: {matricula}')
    print(f'Essa é a média: ''%.2f'%media)
    print(f'Esse é o conceito: {conceito}')

    if conceito in ['A', 'B', 'C']:
        print(f'Essa é a situação: Aprovado')
    else:
        print(f'Essa é a situação: Reprovado')



if __name__ == '__main__':
    main()