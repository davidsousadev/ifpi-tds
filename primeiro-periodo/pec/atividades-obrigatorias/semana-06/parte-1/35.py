'''Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:

Valor para pagamento à vista, com desconto de 9%.
Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
Valor da prestação para pagamento em 10 vezes, com 17% de juros.
'''

def valor(valor):
    av = valor-((valor/100)*9)
    ap5 = valor/5
    ap10 = ((valor + ((valor/100)*17))/10)
    return av, ap5, ap10

def main():
    av, ap5, ap10 = valor(float(input("Digite o valor do produto:")))
    print(f'Valor a vista com 9% de desconto:','%.2f'%av)
    print(f'Valor das parcelas dividido em 5 vezes sem juros:','%.2f'%ap5)
    print(f'Valor das parcelas dividido em 10 vezes com juros de 17%','%.2f'%ap10)
    

if __name__ == '__main__':
    main()