'''
Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, será executada:

1 – Adição

2 – Subtração

3 – Multiplicação

4 – Divisão

Calcule e escreva o resultado dessa operação sobre os dois valores lidos.
'''

def verifica(n1, n2, operacao):
    
    if(operacao==1):
        return n1+n2
    elif(operacao==2): 
        return n1-n2
    elif(operacao==3): 
        return n1*n2
    elif(operacao==4): 
        operacao = round(n1/n2, 2)
        return operacao



def main():
    print("Esse programa simula uma claculadora com operações basicas entre dois numeros.")
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundoo número:"))
    operacao = int(input("Digite a operação sendo: 1 – Adição, 2 – Subtração, 3 – Multiplicação, 4 – Divisão: "))
    resultado = verifica(n1, n2, operacao)
    print(f'Esse é o resultado dessa operação: {resultado}')



if __name__ == '__main__':
    main()