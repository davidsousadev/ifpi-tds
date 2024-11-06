"""

6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um 
programa  que  calcule  e  exiba  o faturamento que  é igual a  quantidade  x preço. Calcule  e exiba 
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos 
e quantos faturamentos estão abaixo da média.

"""

from random import *

max_itens = 20

def quantidadesProdutos(quantiidades, x):
    quantidades.append(int(input(f"Quantidade do produto {x + 1}: ")))
    return quantidades[x]
    
    
def precosProdutos(precos, x):
    precos.append(float(input(f"Preço do produto {x + 1}: "))) 
    return precos[x]
    
def faturamentoProdutos(quantidades, precos):
    faturamentos = []
    for x in range(max_itens):
        faturamentos.append((quantidadesProdutos(quantidades, x)) * (precosProdutos(precos, x)))
    return faturamentos

def verificaAbaixoDaMedia(media_faturamento, faturamentos):
    abaixo_media = 0
    for x in faturamentos:
        if x < media_faturamento:
            abaixo_media += 1
    return abaixo_media
    
while True:
    try:
        quantidades = []
        precos = []
        
        faturamentos = faturamentoProdutos(quantidades, precos)
        faturamento_total = sum(faturamentos)
        media_faturamento = faturamento_total / max_itens
        abaixo_media = verificaAbaixoDaMedia(media_faturamento, faturamentos)

        print("Faturamentos:", faturamentos)
        print("Faturamento total:", faturamento_total)
        print("Média dos faturamentos:", media_faturamento)
        print("Quantidade de faturamentos abaixo da média:", abaixo_media)

        break 
    except ValueError:
        print("\n Número invalido! \n")
