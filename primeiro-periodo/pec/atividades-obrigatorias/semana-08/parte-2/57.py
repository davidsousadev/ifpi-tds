'''
02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.

'''



def somarDigitos(numero):
    soma = 0
    if 0 <= numero < 100000:
        while numero > 0:
            soma += numero % 10
            numero //= 10
        return soma
    else:
        return -1



def main():
    numero = int(input("Digite um número: "))
    soma = somarDigitos(numero)
    print(f'Essa e a o resultado da soma dos digitos: {soma}')



if __name__ == '__main__':
    main()