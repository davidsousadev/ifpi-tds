'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma consoante ou o valor booleano False (falso) caso contrário.

'''
def alfabeto(s):
    if (s == 'a'or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A'or s == 'E' or s == 'I' or s == 'O' or s == 'U'):
        s = False
    elif(s.isalpha()):
        s = True
    else:
        s = False
    return s

def main():
    s = str(input().strip())
    print(alfabeto(s))
    
if __name__ == '__main__':
    main()
