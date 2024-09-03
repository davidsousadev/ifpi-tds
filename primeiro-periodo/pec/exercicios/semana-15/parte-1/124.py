# Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo: Veja o exemplo para a leitura de 50000 para a população: CIDADES COM MAIS DE 50000 HABITANTES: IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639 IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398 IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323 ...

def carrega_cidades(valor):
    resultado = []
    aniversariantes = []
    print(f"CIDADES COM MAIS DE {valor} HABITANTES:")
    with open('ifpi/pec/exercicios/semana-15/parte-1/cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(pop)>=valor:
                print(f"IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}", end="")
    arquivo.close()
    
    return aniversariantes 

    
def main():
    valor = int(input("Digite o valor da quantidade de habitantes: "))
    cidades = carrega_cidades(valor)

if __name__=='__main__':
    main()
