# Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
# o maior número lido;
# o menor número lido;
# a média aritmética dos números lidos.
def media(n1, n2, n3,n4, n5):
    media = ((n1 + n2 + n3 + n4 + n5)/5)
    return media



def main():
    print(f'Digite cinco números')
    n1 = int(input(f'Digite o primeiro número: '))
    n2 = int(input(
    f'Digite o segundo número: '
    ))
    n3 = int(input(f'Digite o terceiro número: '))
    n4 = int(input(f'Digite o quarto número: '))
    n5 = int(input(f'Digite o quinto número: '))
    mediaaritimetica = (media(n1, n2, n3, n4, n5))
    maior = (max(n1, n2, n3, n4, n5))
    menor = (min(n1, n2, n3, n4, n5))
    print(f'Esse é o maior número: {maior}')
    print(f'Esse é o menor número: {menor}')
    print(f'Esse é a média aritimética: {mediaaritimetica}')



if __name__ == '__main__':
    main()