'''
Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. 
O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. 
Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. 
Separe esses valores com um hífen.
'''

def verifica(n1, n2):
   return f"QUADRADO" if(n1==n2)  else f"{n1*2+n2*2} - {n1*n2}"
   



def main():
    print("Digite dois valores um para base e outro para altura.")
    n1 = int(input("Digite o valor da base: "))
    n2 = int(input("digite o valor da altura: "))
    msg = verifica(n1, n2)
    if (msg=="QUADRADO"):
        print(f'Esse retângulo é: {msg}')
    else:
        print(f'Esse tem retângulo perímetro - área igual a: {msg}')


    
if __name__ == '__main__':
    main()