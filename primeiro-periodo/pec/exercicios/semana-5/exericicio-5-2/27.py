#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma letra (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

def verificador(x):
    if (x.isalpha()):
        x = True   
    else:
        x = False
    return x
    
def main():
    x = str(input("Digite um caractere:").strip())
    print(verificador(x))

if __name__ == '__main__':
    main()