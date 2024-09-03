'''Escreva um programa que, para um número indeterminado de pessoas:

leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
calcule e escreva o número de pessoas;
calcule e escreva a idade média do grupo;
calcule e escreva a menor idade e a maior idade.'''



def calcular_informacao_de_pessoas():
    idades = 0
    quantidade = 0
    maior = 0
    menor = 0
    while True:
        idade = int(input("Digite a idade de uma pessoa: "))
        if idade == 0 and quantidade > 0:
            media = idades / quantidade
            return quantidade, media, menor, maior 
            break
        quantidade += 1
        idades += idade
        if maior == 0 or idade > maior and idade > menor:
            maior = idade
        if menor == 0 or idade < menor and idade < maior:
            menor = idade


def main():
    print("Esse programa ler idade um número indeterminado de pessoas e exibe dados em relação as idades coletadas.")
    quantidade, media, menor, maior = calcular_informacao_de_pessoas()
    print(f"Quantidade de pessoas: {quantidade}")
    print(f"Media idade média do grupo: {media:.2f}")
    print(f"Menor idade: {menor}")
    print(f"Maior idade: {maior}")




if __name__ == '__main__':
	main()