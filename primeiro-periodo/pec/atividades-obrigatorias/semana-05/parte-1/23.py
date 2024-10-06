'''Escreva um programa que leia um preço e um valor percentual. Informe o preço com o aumento percentual e o preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e o valor percentual de 5 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.'''
preco = float(input())
percentual = float(input())
aumento = (preco+((preco/100)*percentual))
desconto = (preco-((preco/100)*percentual))
print('%.2f'%aumento)
print('%.2f'%desconto)