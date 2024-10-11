'''Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores.

'''
dv = float(input())
ds = float(input())
re = dv // ds
ri = dv % ds
print('%.4f'%re)
print('%.4f'%ri)