'''Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero).'''

def ler_numeros_inteiros_retorna_media():
    soma = 0
    qtd = 0
    while True:
        num = int(input("Escreva um número inteiro positivo: "))
        if num > 0: 
            soma += num
            qtd += 1
        elif(num==0):
            if qtd > 0:
                media = soma / qtd
                return media
            break



def main():
    media = ler_numeros_inteiros_retorna_media()
    print('%.2f'%media)



if __name__ == '__main__':
    main()