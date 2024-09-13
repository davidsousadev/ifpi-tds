# Escreva um programa que leia uma chave e um valor, crie um dicionários com os valores lidos. A leitura de uma chave vazia finaliza a leitura do dicionário. Mostre o dicionário na tela; após, leia novamente uma chave e um valor e atualize o valor da chave no dicionário até que seja feita a leitura de uma chave vazia. Mostre novamente o dicionário na tela.

def atualiza_valores(dicionario):
    while True:
        chave = str(input().strip())
        if not  chave:
             break
        
        if chave in dicionario:
            valor = str(input().strip())
            dicionario[chave] = valor
    return dicionario
    

def ler_valores():
    dicionario= {}
    while True:
        chave = str(input().strip())
        if not chave:
             break
        valor = str(input().strip())
        dicionario[chave] = valor	    
    return dicionario


def main():
    dicionario = ler_valores()
    print(f"{dicionario}")
    atualizacao = atualiza_valores(dicionario)
    print(f"{atualizacao}")
 
 
 
if __name__ =='__main__':
	main()