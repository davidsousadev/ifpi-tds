'''
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero).'''



def numero_maior_menor(maior, menor):
	while True:
		num = int(input("Escreva um número inteiro positivo: "))
		if num == 0:
			return maior, menor
			break
		if num > maior:
			maior = num
		if num < menor:
			menor = num 	



def main():
	num = int(input("Escreva um número inteiro positivo: "))
	maior = num
	menor = num
	maior, menor = numero_maior_menor(maior, menor)
	print(f"Esse é o maior número: {maior}")
	print(f"Esse é o menor número: {menor}")


if __name__ == '__main__':
	main()