'''Escreva um programa que leia dois valores e mostre na tela, nessa ordem:

a. A soma dos números;

b. A concatenação das strings;

c. A multiplicação dos números;

d. A multiplicação como strings;

e. A divisão dos números;

f. A divisão inteira dos números;

g. A exponenciação;

h. O módulo (resto).'''
a = float(input())
b = int(input())
print('%.1f'%(a+b))
print(str(a)+str(b))
print(f'{a*b}')
print(str(a)*int(b))
print(f'{a/b}')
print('%.1f'%(a//b))
print(f'{a**b}')
print(f'{a%b}')