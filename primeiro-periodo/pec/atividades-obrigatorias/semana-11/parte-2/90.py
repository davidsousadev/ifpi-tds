'''
Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar uma nota válida, o aluno deve ver seu conceito, segundo a tabela:

Conceito	Nota
A	>= 8,5
B	>= 7,0
c	>= 5,0
D	>= 4,0
E	>= 0,0
'''



def conceito_nota(nota):
    if nota >= 8.5:
        conceito = 'A'
    elif nota >= 7.0:
        conceito = 'B'
    elif nota >= 5.0:
        conceito = 'C'
    elif nota >= 4.0:
        conceito = 'D'
    else:
        conceito = 'E'
    return conceito



def main(): 
    print("O programa ler a nota de um aluno, entre zero e dez:")
    while True:
        nota = float(input("Digite a nota do aluno: "))
        if nota >= 0 or nota <= 10:
            conceito = conceito_nota(nota)
        if nota < 0 or nota > 10:
    	    print("Nota inválida.")
        else:
            break
    print(f"Esse é o conceito do aluno: {conceito}")



if __name__ == '__main__':
    main()