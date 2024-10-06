'''Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou o valor booleano False (falso) caso contrário.
'''
def main():
                n = int(input("Digite um número: "))
                print("Se for impar True se par False\n")
                if(n%2==0):           
                                print(False)
                else:
                                print(True)



if __name__ == '__main__':
    main()