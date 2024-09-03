'''
02. Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual
delas é a mais recente.

'''




def verifica(dia1, mes1, ano1, dia2, mes2, ano2):
    if(mes1 <= mes2 and dia1 < dia2):
        maiordia = dia2
        maiormes = mes2
        maiorano = ano2
    else:
        maiordia = dia1
        maiormes = mes1
        maiorano = ano1 

    return maiordia, maiormes, maiorano


def main():
    dia1 = int(input("Digite o dia da data 1: "))
    mes1 = int(input("Digite o mês da data 1: "))
    ano1 = int(input("Digite o ano da data 1: "))
    dia2 = int(input("Digite o dia da data 2: "))
    mes2 = int(input("Digite o mês da data 2: "))
    ano2 = int(input("Digite o ano da data 2: "))
    maiordia, maiormes, maiorano = verifica(dia1, mes1, ano1, dia2, mes2, ano2)
    print(f'Essa é a data mais atual {maiordia}/{maiormes}/{maiorano}.') 



if __name__ == '__main__':
    main()