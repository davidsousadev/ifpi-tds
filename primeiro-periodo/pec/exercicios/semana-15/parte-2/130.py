# Faça um programa que leia e armazene em um array tridimensional contendo os valores do faturamento anual de uma empresa, especificados por filial e também mês a mês. Veja a estrutura do array na imagem anexa. Após a leitura dos dados faça o seguinte:

# Calcule o total de cada ano por filial;
# Calcule o total de todas as filiais por ano;
# Calcule o total do período para todas as filiais;
# Mostre todos os dados lidos e calculados de acordo com o período que ocorrer, por exemplo:
#     2014;Filial 1;Janeiro;210
#     ...
#     2014;Filial 1;Dezembro;463
#     TOTAL 2014 FILIAL 1;3526
#     2014;Filial 2;Janeiro;430
#     ...
#     2014;Filial 3;Dezembro;310
#     TOTAL 2014 FILIAL 3;3346
#     TOTAL 2014 TODAS FILIAIS;10727
#     2015;Filial 1;Janeiro;316
#     ...
#     2017;Filial 3;Dezembro;354
#     TOTAL 2017 FILIAL 3;3550
#     TOTAL 2017 TODAS FILIAIS;11123
#     TOTAL PERÍODO TODAS FILIAIS;42855

def ler_faturamento():
    filiais = 3  
    meses = 12   
    anos = 4     
    faturamento = [[[0 for _ in range(meses)] for _ in range(filiais)] for _ in range(anos)]

    for ano in range(anos):
        for filial in range(filiais):
            for mes in range(meses):
                valor = int(input(f"Digite o valor do faturamento da filial {filial+1} no ano {ano+1} mes {mes+1}: "))
                faturamento[ano][filial][mes] = valor

    return faturamento

def calcular_total_ano_filial(faturamento, ano, filial):
    return sum(faturamento[ano - 2014][filial])

def calcular_total_todas_filiais_por_ano(faturamento, ano):
    return sum(calcular_total_ano_filial(faturamento, ano, filial) for filial in range(len(faturamento[0])))

def calcular_total_periodo_todas_filiais(faturamento):
    return sum(calcular_total_todas_filiais_por_ano(faturamento, ano) for ano in range(len(faturamento)))

def exibir_resultados(faturamento):
    total_periodo_todas_filiais = int()
    for ano in range(len(faturamento)):
        for filial in range(len(faturamento[0])):
            for mes in range(len(faturamento[0][0])):
                print(f"{ano + 2014};Filial {filial + 1};{meses[mes]};{faturamento[ano][filial][mes]}")
            total_ano_filial = calcular_total_ano_filial(faturamento, ano + 2014, filial)
            print(f"TOTAL {ano + 2014} FILIAL {filial + 1};{total_ano_filial}")
        total_todas_filiais_por_ano = calcular_total_todas_filiais_por_ano(faturamento, ano + 2014)
        print(f"TOTAL {ano + 2014} TODAS FILIAIS;{total_todas_filiais_por_ano}")
        total_periodo_todas_filiais += total_todas_filiais_por_ano
    return total_periodo_todas_filiais
    

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def main():
    faturamento = ler_faturamento()
    total_periodo_todas_filiais = exibir_resultados(faturamento)
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo_todas_filiais}")
    
if __name__ == "__main__":
    main()
