'''Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 para identificar masculino e 2 para identificar feminino.
'''
def main():
                nome = str(input("Digite seu nome:").strip())
                sexo = int(input("Digite seu sua opção sexual: número 1 para masculino e 2 para feminino."))
                if(sexo==1):
                                print(f'Ilmo Sr. {nome}')
                else:
                                print(f'Ilma Sra. {nome}')



if __name__ == '__main__':
    main()