'''Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:

def calcular(a, b, c):
    return 2 * a + 5 * b - c
'''

def calcular(a, b, c):
    return (2 * a + 5 * b - c)
a = int(input())
b = int(input())
c = int(input())
print (calcular(a, b, c))