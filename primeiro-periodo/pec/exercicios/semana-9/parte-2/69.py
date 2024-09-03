'''
Um sacolão está vendendo frutas com a seguinte tabela de preços:

Item|Até 5Kg|Acima de 5Kg

:--------- |:-------------:| :----------:

Morango | R$ 2,50 | R$ 2,20

Maça | R$ 1,80 | R$ 1,50

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
def quantidade(pesoMorango, pesoMaca):
    if pesoMorango <= 5:
        valorMorango = pesoMorango * 2.50
    else:
        valorMorango = pesoMorango * 2.20
    if pesoMaca <= 5:
        valor_maca = pesoMaca * 1.80
    else:
        valor_maca = pesoMaca * 1.50
    valorTotal = valorMorango + valor_maca
    if (((pesoMorango + pesoMaca) > 8) or (valorTotal > 25)):
        desconto = 0.10 * valorTotal
    else:
        desconto = 0
    valorTotal += (-desconto)
    return valorTotal



def main():
    print(f"Digite o peso das frutas: ")
    print("Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10 ""%"" sobre este total.")
    pesoMorango = float(input("Qaul o peso do morango: "))
    pesoMaca = float(input("Qual o peso da maça: "))
    valorTotal = quantidade(pesoMorango, pesoMaca)
    print(f'O valor total da compra é: ''%.2f'%valorTotal)



if __name__ == '__main__':
    main()