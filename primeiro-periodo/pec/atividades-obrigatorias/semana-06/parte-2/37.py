'''Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso! Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro mais próximo e imprima o resultado.

'''

def main():
    num = round(float(input("Digite um número: ")))
    print(f'Este é o número inteiro mais proximo: {num}')



if __name__ == '__main__':
    main()