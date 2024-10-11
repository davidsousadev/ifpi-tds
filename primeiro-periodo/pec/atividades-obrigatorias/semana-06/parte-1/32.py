'''Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.'''

def main():
    s = str(input("Digite um caractere: "))
    cn = ord(s)
    print(f'Esse e o código numérico {cn} correspondente a: {s}')

if __name__ == '__main__':
    main()
    