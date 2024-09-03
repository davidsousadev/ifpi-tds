'''
Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:

Todos os valores são diferentes;

Existem dois valores iguais e um diferente;

Todos os valores são iguais.
'''



def verifica(n1, n2, n3):
    if(n1==n2 and n2==n3):
        return 'Todos os valores são iguais'
    elif(n1!=n2 and n2!=n3 and n1!=n3): 
        return 'Todos os valores são diferentes'
    else:
        return 'Existem dois valores iguais e um diferente'



def main():
    print("Digite três números inteiros.")
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundoo número:"))
    n3 = int(input("Digite o terceiro número:"))
    msg = verifica(n1, n2, n3)
    print(f'Foi verificado que: {msg}')



if __name__ == '__main__':
    main()