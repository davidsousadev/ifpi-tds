'''
Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).
'''
def media_de_numeros():
    media = 0
    for i in range(1,101):
        x = int(input())
        media += x
    return media/100 


   
def main():
    print(media_de_numeros())



if __name__ == '__main__':
    main()