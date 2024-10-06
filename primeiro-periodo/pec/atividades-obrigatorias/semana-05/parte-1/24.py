'''Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertidade para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.'''
min = int(input())
h = min//60
min = min%60
print(f'{h}:{min}')
