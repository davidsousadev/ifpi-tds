'''Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.


'''

def main():
                s = str(input("Digite um caractere: "))
                print("Esse caractere é: ")
                if(s in 'AEIOUaeiou' and s !=''):
                                print('vogal')
                elif('a' <= s <= 'z' or 'A' <= s <= 'Z'):
                                print('consoante')
                elif('0' <= s <= '9'):
                                print('número')
                else:
                                print('símbolo')



if __name__ == '__main__':
    main()