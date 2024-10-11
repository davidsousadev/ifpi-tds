'''Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação: A condição de saída do laço será a leitura do valor 0 (flag).'''



def soma_de_numeros_inteiros():
    soma = 0
    while True:
        num = int(input("Digite um número inteiro: "))    
        if num == 0:
            return soma
            break
        soma += num



def main():
    print("Esse programa ler uma quantidade indeterminada de números inteiros e retorna a soma deles.")
    soma = soma_de_numeros_inteiros()
    print(f"Essa é a soma dos números {soma}.")



if __name__ == '__main__':
	main()