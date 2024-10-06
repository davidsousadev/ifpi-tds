'''Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas! Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:

Fahrenheit = (Celsius x (9 / 5)) + 32'''

def converter(c):
	fahrenheit = ((c * (9/5)) + 32)
	return fahrenheit 
	

	
def main():
    celsius = float(input("Digite a quantidade de graus Celsius: "))
    fahrenheit = converter(celsius)
    print(f'Este e o valor corespondente em Fahrenheit: ','%.2f'%fahrenheit)



if __name__ == '__main__':
    main()