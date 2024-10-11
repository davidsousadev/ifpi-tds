'''Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.'''

pi =3.141592
r = float(input())
c = (2*pi*r)
a = (pi * (r**2))
ase = (4*a)
v = (4/3)*(pi*(r**3))
print('%.6f'%c)
print('%.6f'%a)
print('%.6f'%ase)
print('%.6f'%v)