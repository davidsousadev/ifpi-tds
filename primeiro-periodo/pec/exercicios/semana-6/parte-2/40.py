def converter(c):
	fahrenheit = ((c * (9/5)) + 32)
	return fahrenheit 
	

	
def main():
    celsius = float(input("Digite a quantidade de graus Celsius: "))
    fahrenheit = converter(celsius)
    print(f'Este e o valor corespondente em Fahrenheit: ','%.2f'%fahrenheit)



if __name__ == '__main__':
    main()