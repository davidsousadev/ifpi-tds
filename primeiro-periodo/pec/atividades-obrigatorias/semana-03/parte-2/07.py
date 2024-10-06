'''Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado para duas casas decimais.

'''
num1 = float(input())
num1 = (num1 - (num1/100) * 10)
print('%.2f'%num1)