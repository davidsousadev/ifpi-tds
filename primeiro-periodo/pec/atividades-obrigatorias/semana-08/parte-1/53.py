'''
03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
são diferentes. NÃO use as funções embutidas min() e max().
'''



def soma(n1, n2, n3, n4, n5):
    if(n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5):
        maior = n1
    elif(n2>=n3 and n2>=n4 and n2>=n5):
        maior = n2
    elif(n3>=n4 and n3>=n5):
        maior = n3
    elif(n4>=n5):
        maior = n4
    else:
        maior = n5
    if(n1<=n2 and n1<=n3 and n1<=n4 and n1<=n5):
        menor = n1
    elif(n2<=n3 and n2 <=n4 and n2<=n5):
        menor = n2
    elif(n3<=n4 and n3<=n5):
        menor = n3
    elif(n4<=n5):
        menor = n4
    else:
        menor = n5       
    return maior, menor




def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))
    n5 = int(input("Digite o quinto número: "))
    maior, menor = soma(n1, n2, n3, n4, n5)
    print(f'Esse e o maior número {maior}.')
    print(f'Esse e o menor número {menor}.')



if __name__ == '__main__':
    main()