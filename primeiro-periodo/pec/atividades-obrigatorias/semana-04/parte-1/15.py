'''Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima:

Área do piso da sala: largura * comprimento

Volume da sala: largura * comprimento * altura

Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento'''
altura = int(input())
comprimento = int(input())
largura = int(input())
areaPiso = largura * comprimento
volume = altura * largura * comprimento
areaParede = (2 * altura * largura + 2 * altura * comprimento)
print (f'{areaPiso}')
print (f'{volume}')
print (f'{areaParede}')