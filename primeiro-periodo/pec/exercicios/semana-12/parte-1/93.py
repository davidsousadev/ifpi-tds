'''Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.'''



def ultrapassagemDePopulacao(natalidadePopulacaoA, natalidadePopulacaoB):
    contadorDeTempo = 0
    if natalidadePopulacaoA > natalidadePopulacaoB:
        while natalidadePopulacaoA > natalidadePopulacaoB:
            natalidadePopulacaoA = natalidadePopulacaoA + (natalidadePopulacaoA/100) * 2
            natalidadePopulacaoB = natalidadePopulacaoB + (natalidadePopulacaoB/100) * 3
            contadorDeTempo += 1
    else:
	    while natalidadePopulacaoA < natalidadePopulacaoB:
	       	natalidadePopulacaoA = natalidadePopulacaoA + (natalidadePopulacaoA/100) * 3
	       	natalidadePopulacaoB = natalidadePopulacaoB + (natalidadePopulacaoB/100) * 2
	       	contadorDeTempo += 1 
    return contadorDeTempo



def main():
    natalidadePopulacaoA = int(input("Digite a natalidade da população A: "))
    natalidadePopulacaoB = int(input("Digite a natalidade da população B: "))
    ultrapassagem = ultrapassagemDePopulacao(natalidadePopulacaoA, natalidadePopulacaoB)       		      
    print(f"O tempo necessário para que a população do país B ultrapasse a população do país A e de {ultrapassagem} anos.")



if __name__ == '__main__':
    main()