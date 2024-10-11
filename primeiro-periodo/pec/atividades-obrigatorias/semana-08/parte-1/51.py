'''
01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de
nascimento de uma pessoa, calcule e escreva a idade exata em anos
'''



def verificaIdade(diaAtual, mesAtual, anoAtual, diaNascimento, mesNascimento, anoNascimento):
    idade = anoAtual-anoNascimento
    if(mesAtual <= mesNascimento and diaAtual < diaNascimento):
        idade -= 1
    return idade



def main():
    diaAtual = int(input("Digite o dia atual: "))
    mesAtual = int(input("Digite o mês atual: "))
    anoAtual = int(input("Digite o ano atual: "))
    diaNascimento = int(input("Digite o dia de nascimento: "))
    mesNascimento = int(input("Digite o mês de nascimento: "))
    anoNascimento = int(input("Digite o ano de nascimento: "))
    idade = verificaIdade(diaAtual, mesAtual, anoAtual, diaNascimento, mesNascimento, anoNascimento)
    print(f'São {idade} de idade.') 



if __name__ == '__main__':
    main()