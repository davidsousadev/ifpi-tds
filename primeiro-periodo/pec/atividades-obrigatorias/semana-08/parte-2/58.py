'''

03. Escreva um programa que leia um número inteiro positivo e escreva na tela:

• FIZZ se o número é divisível por três;
• BUZZ se o número é divisível por cinco;
• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
• O próprio número caso não seja divisível por três ou por cinco.
OBS: para cada número lido apenas uma resposta deve ser impressa.

'''



def verificarDivisiveis(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FIZZBUZZ"
    elif numero % 3 == 0:
        return "FIZZ"
    elif numero % 5 == 0:
        return "BUZZ"
    else:
        return numero



def main():
    numero = int(input("Digite um número: "))
    numero = verificarDivisiveis(numero)
    print(f'Esse é o resultado da verificação do número: {numero}')
    print(f'''
        • FIZZ se o número é divisível por três;
        • BUZZ se o número é divisível por cinco;
        • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
        • O próprio número caso não seja divisível por três ou por cinco.    
    ''')



if __name__ == '__main__':
    main()