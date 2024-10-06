# Escreva um programa que leia três lados para um triânculo
# e mostre uma das mensagens:
#   - é triangulo equilátero
#   - é triangulo isósceles
#   - é triangulo escaleno
#   - não é triângulo

def e_triangulo(a, b, c):
    # Sem funções; Com operadores lógicos
    # Testa se são os lados são válidos para um triângulo
    if (a < b + c) and (b < a + c) and (c < a + b):
        # É equilátero
        if (a == b) and (b == c):
            return 'é triangulo equilátero'

        #É isósceles
        if (a == b) or (b == c) or (a == c):
            return 'é triangulo isósceles'

        # É escaleno
        if (a != b) and (b != c):
            return 'é triangulo escaleno'
    else:
        return 'não é triângulo' 

def main():
    # a = float(input('a: '))
    # b = float(input('b: '))
    # c = float(input('c: '))
    
    print('Teste de Equilátero')
    a, b, c = 2, 2, 2 # Equilátero
    print(e_triangulo(a, b, c))

    print('\nTeste de Isósceles Caso 1')
    a, b, c = 3, 2, 2 # Isósceles Caso 1
    print(e_triangulo(a, b, c))

    print('\nTeste de Isósceles Caso 2')
    a, b, c = 2, 3, 2 # Isósceles Caso 2
    print(e_triangulo(a, b, c))

    print('\nTeste de Isósceles Caso 3')
    a, b, c = 2, 2, 3 # Isósceles Caso 3
    print(e_triangulo(a, b, c))

    print('\nTeste de Escaleno')
    a, b, c = 3, 4, 5 # Escaleno
    print(e_triangulo(a, b, c))

    print('\nTeste de Não é triângulo Caso 1')
    a, b, c = 9, 4, 5 # Não é triângulo
    print(e_triangulo(a, b, c))

    print('\nTeste de Não é triângulo Caso 2')
    a, b, c = 3, 9, 5 # Não é triângulo
    print(e_triangulo(a, b, c))

    print('\nTeste de Não é triângulo Caso 3')
    a, b, c = 3, 4, 9 # Não é triângulo
    print(e_triangulo(a, b, c))

if __name__ == '__main__':
    main()