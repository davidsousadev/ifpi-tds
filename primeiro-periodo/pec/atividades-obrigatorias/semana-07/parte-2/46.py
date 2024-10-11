'''Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).

'''

def verificarestadocivil(estadocivil):
    if(estadocivil==1):
        return True
    else:
        return False

def main():
    nome = str(input("Digite seu nome completo: ").strip())
    estadocivil = int(input("Digite seu estado civil (Considere apenas “1” para casado e “2” para solteiro): "))
    estadocivil = verificarestadocivil(estadocivil)
    if(estadocivil == True):
        conjuge = str(input("Digite o nome completo do seu cônjuge: ").strip())
        contador = len(nome) + len(conjuge)
        print('Essa é a quantidade total de caracteres no(s) nome(s) lido(s): %.0f'%contador)
    else:
         print('Essa é a quantidade total de caracteres no nome lido: %.0f'%len(nome))



if __name__ == '__main__':
    main()
