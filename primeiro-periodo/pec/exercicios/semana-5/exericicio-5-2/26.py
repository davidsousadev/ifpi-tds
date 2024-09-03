#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma vogal ou o valor booleano False (falso) caso contrário.

def verificador(x):
    if (x == 'a'or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A'or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        x = True
    else:
        x = False
    return x


def main():
    x = str(input("Digite um caractere:").strip())
    print(verificador(x))

if __name__ == '__main__':
    main()