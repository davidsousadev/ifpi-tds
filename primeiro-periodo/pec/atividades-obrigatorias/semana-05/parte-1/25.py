'''Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.'''
num = int(input())
num = str(num)
num = num[::-1]
print(f'{num}')