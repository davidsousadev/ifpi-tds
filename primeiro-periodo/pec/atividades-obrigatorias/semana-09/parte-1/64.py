'''
Escreva um programa que leia 3 valores inteiros. 
Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, 
imprimindo o valor da diferença.
'''

def verifica(n1, n2, n3):
    v1 = abs(n1-n2)
    v2 = abs(n1-n3)
    return  v2 if v2 < v1 else v1



def main():
    print("Digite três numeros inteiros.")
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundoo número:"))
    n3 = int(input("Digite o terceiro número:"))
    msg = verifica(n1, n2, n3)
    print(f'A menor diferença em relação ao primeiro número é: {msg}')



    
if __name__ == '__main__':
    main()