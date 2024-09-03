'''
04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
média. Considere duas casas decimais.
'''



def mediaAritimetica(n1, n2, n3, n4, n5):
    media = (n1+n2+n3+n4+n5)/5
    return media




def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))
    n5 = int(input("Digite o quinto número: "))
    media = mediaAritimetica(n1, n2, n3, n4, n5)
    print(f'Essa e a média ''%.2f'%media)
    print(f'Essses mumeros estão acima da média.')
    if(n1>media):
        print('%.2f'%n1)
    if(n2>media):
        print('%.2f'%n2)
    if(n3>media):
        print('%.2f'%n3)
    if(n4>media):
        print('%.2f'%n4)
    if(n5>media):
        print('%.2f'%n5)
    




if __name__ == '__main__':
    main()