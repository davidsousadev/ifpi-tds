# Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês informado. Veja o exemplo para o mês com valor 4 e 50000 para a população: CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL: Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril. Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril. Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril. Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril. ...

def carrega_cidades(mesA, valor):
    resultado = []
    aniversariantes = []
    print(f"CIDADES COM MAIS DE {valor} HABITANTES E ANIVERSÁRIO EM {meses(mesA)}:")
    with open('ifpi/pec/exercicios/semana-15/parte-1/cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(pop)>=valor and int(mes)==mesA:
                print(f"{nome}({uf}) tem {int(pop)} habitantes e faz aniversário em {dia} de {meses(mesA).lower()}.")
    arquivo.close()
    
    return aniversariantes 

def meses(mes):
    if (mes == 1):
        return "JANEIRO"
    elif (mes == 2):
        return "FEVEREIRO"
    elif (mes == 3):
        return "MARÇO"
    elif (mes == 4):
        return "ABRIL"
    elif (mes == 5):
        return "MAIO"
    elif (mes == 6):
        return "JUNHO"
    elif (mes == 7):
        return "JULHO"
    elif (mes == 8):
        return "AGOSTO"
    elif (mes == 9):
        return "SETEMBRO"
    elif (mes == 10):
        return "OUTUBRO"
    elif (mes == 11):
        return "NOVEMBRO"
    elif (mes == 12):
        return "DEZEMBRO"
    
def main():
    mes = int(input("Digite o mes: "))
    valor = int(input("Digite o valor da quantidade de habitantes: "))
    cidades = carrega_cidades(mes, valor)

if __name__=='__main__':
    main()
