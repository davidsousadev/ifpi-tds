def calcula(maca, banana):
	maca *= 3
	banana *= 2
	soma = maca + banana
	return soma

def main():
    maca = float(input("Digite o valor unitario da maça: "))
    banana = float(input("Digite o valor unitario da banana: "))
    soma = calcula(maca, banana)
    print(f'A soma dos valores de 3 maças e duas bananas é igual a: ', '%.2f'%soma)
    



if __name__ == '__main__':
    main()