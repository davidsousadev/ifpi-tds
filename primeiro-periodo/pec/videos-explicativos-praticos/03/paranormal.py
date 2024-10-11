from random import randrange

input('Pense em um número de 1 a 100. ENTER para continuar...')
n = randrange(100) + 1

a = randrange(1, 6)
input(f'Some o número pensado com {a}. ENTER para continuar...')
resultado = n + a

b = randrange(5, 11)
input(f'Some o resultado com {b}. ENTER para continuar...>')
resultado = resultado + b

input(f'Diminua o primeiro número que pensou. ENTER para continuar...')
resultado = resultado - n

c = randrange(2, 5)
input(f'Multiplique o resultado por {c}. ENTER para continuar...>')
resultado = resultado * c

print(f'O resultado é {resultado}')