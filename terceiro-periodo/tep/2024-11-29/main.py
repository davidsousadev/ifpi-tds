import os
import numpy as np


# 1. Carregamento do Dataset:
# Função para listar e carregar os arquivos CSV
def carregar_datasets():
    arquivos = [f for f in os.listdir('.') if f.startswith('station_') and f.endswith('.csv')]
    if not arquivos:
        print("Nenhum arquivo CSV encontrado.")
        return None
    
    dados_cidades = {}
    
    for arquivo in arquivos:
        # Importe o arquivo utilizando o método numpy.loadtxt, ignorando a primeira linha (cabeçalho).
        cabecalho = np.genfromtxt(arquivo, delimiter=',', max_rows=1, dtype=str)
        # Converta as colunas de temperaturas para um array NumPy (ignorando a coluna de datas).
        dados = np.loadtxt(arquivo, delimiter=',', skiprows=1, usecols=range(1, 13))
        anos = np.loadtxt(arquivo, delimiter=',', skiprows=1, usecols=0, dtype=int)
        
        dados[dados == 999.90] = np.nan
        
        cidade = arquivo.split('.')[0]
        dados_cidades[cidade] = {'anos': anos, 'dados': dados}
    
    return dados_cidades
dados_cidades = carregar_datasets()


# 2. Manipulação dos Dados:
# Use as funcionalidades do NumPy para processar e analisar os dados.

# Função para realizar as análises por cidade
def analises_cidade(dados_cidades):
    resultados = []
    cidade_maior_variacao = None
    maior_variacao_valor = 0
    
    
    # 3. Produza pelo menos 5 relatórios (insights):
    # Nome dos meses da primeira linha
    meses_nome = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    
    for cidade, dados in dados_cidades.items():
        anos = dados['anos']
        temperatura = dados['dados']
        
        mes_quente_total = None
        temp_mes_quente = -np.inf
        ano_mes_quente = None
        
        mes_frio_total = None
        temp_mes_frio = np.inf
        ano_mes_frio = None
        
        meses_below_20 = 0
        meses_above_38 = 0
        
        # Iterar pelos anos e meses
        for i, ano in enumerate(anos):
            for j, mes in enumerate(meses_nome):
                temp_mes = temperatura[i, j]
                
                # Encontre o mês mais quente e o mês mais frio em todo o período para cada cidade.
                
                # Identificar o mês mais quente
                if temp_mes > temp_mes_quente:
                    temp_mes_quente = temp_mes
                    mes_quente_total = mes
                    ano_mes_quente = ano
                
                # Identificar o mês mais frio
                if temp_mes < temp_mes_frio:
                    temp_mes_frio = temp_mes
                    mes_frio_total = mes
                    ano_mes_frio = ano
                    
                # Determine o número de meses em que a temperatura foi abaixo de 20°C para cada cidade.
                
                if temp_mes < 20:
                    meses_below_20 += 1
                
                # Determine o numero de meses em que a temperatura foi acima de 38° para cada cidade    
                if temp_mes > 38:
                    meses_above_38 += 1
        
        # Calcule a média de temperatura de todas as cidades entre os anos de 2000 a 2019.
        temperaturas_2000_2019 = []
        for i, ano in enumerate(anos):
            if 2000 <= ano <= 2019:
                # Adicionar apenas temperaturas válidas (não nan)
                valid_temperatures = temperatura[i, :][~np.isnan(temperatura[i, :])]
                temperaturas_2000_2019.extend(valid_temperatures)
        
        if temperaturas_2000_2019:
            media_temperatura_2000_2019 = np.mean(temperaturas_2000_2019)
        else:
            media_temperatura_2000_2019 = 'Não disponível'
        
        # Identifique a cidade com a maior variação de temperatura ao longo do período analisado.
        variacao_temp = np.nanmax(temperatura) - np.nanmin(temperatura)
        
        # Verificar se a variação é maior que a maior variação encontrada
        if variacao_temp > maior_variacao_valor:
            maior_variacao_valor = variacao_temp
            cidade_maior_variacao = cidade
        
        # Guardar os resultados para a cidade
        resultados.append({
            'Cidade': cidade,
            'Mes Mais Quente': mes_quente_total,
            'Temperatura Mes Mais Quente': temp_mes_quente,
            'Ano Mes Mais Quente': ano_mes_quente,
            'Mes Mais Frio': mes_frio_total,
            'Temperatura Mes Mais Frio': temp_mes_frio,
            'Ano Mes Mais Frio': ano_mes_frio,
            'Meses Abaixo de 20°C': meses_below_20,
            'Meses Acima de 38°C': meses_above_38,
            'Média Temperatura 2000-2019': f"{media_temperatura_2000_2019:.2f}",
            'Variação de Temperatura': f"{variacao_temp:.2f}"
        })
    
    return resultados, cidade_maior_variacao, maior_variacao_valor

# Realizar as análises
resultados, cidade_maior_variacao, maior_variacao_valor = analises_cidade(dados_cidades)

# 4. Apresente os Resultados:
# Exiba os resultados em uma interface simples
for resultado in resultados:
    print(f"Cidade: {resultado['Cidade']}")
    print(f"  Mês mais quente: {resultado['Mes Mais Quente']} ({resultado['Ano Mes Mais Quente']}) - Temperatura: {resultado['Temperatura Mes Mais Quente']}°C")
    print(f"  Mês mais frio: {resultado['Mes Mais Frio']} ({resultado['Ano Mes Mais Frio']}) - Temperatura: {resultado['Temperatura Mes Mais Frio']}°C")
    print(f"  Meses abaixo de 20°C: {resultado['Meses Abaixo de 20°C']} meses.")
    print(f"  Meses acima de 38°C: {resultado['Meses Acima de 38°C']} meses")
    print(f"  Média de Temperatura 2000-2019: {resultado['Média Temperatura 2000-2019']}°C")
    print(f"  Variação de Temperatura: {resultado['Variação de Temperatura']}°C")
    print()

print(f"A cidade com maior variação de temperatura foi: {cidade_maior_variacao} com {maior_variacao_valor:.2f}°C")
