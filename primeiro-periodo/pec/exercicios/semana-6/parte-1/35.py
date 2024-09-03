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