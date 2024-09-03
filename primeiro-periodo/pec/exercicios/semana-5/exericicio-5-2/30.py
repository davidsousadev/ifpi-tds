#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.

def verificador(x):
    if (x.isdecimal()):
        x = False
    elif(s.isalpha()):
        x = False
    else:
        x = True
    return x

def main():
    x = str(input("Digite um caractere:").strip())
    print(verificador(x))
    
if __name__ == '__main__':
    main()
