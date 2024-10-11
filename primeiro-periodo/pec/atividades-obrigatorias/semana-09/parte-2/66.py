'''
Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.
'''
def verificaDia(dia):
    if(dia==1):
        return f"domingo"
    elif(dia==2):
        return f"segunda-feira"
    elif(dia==3):
        return f"terça-feira"
    elif(dia==4):
        return f"quarta-feira"
    elif(dia==5):
        return f"quinta-feira"
    elif(dia==6):
        return f"sexta-feira"
    elif(dia==7):
        return f"sábado"
    else:
        return f"valor inválido"



def main():
    dia = int(input("Digite o número do dia da semana(1-domingo, 2-segunda-feira, 3-terça-feira etc.): "))
    dia = verificaDia(dia)   
    print(f"Esse dia é : {dia}.")



if __name__ == '__main__':
    main()