# Uma pista de Kart permite 5 voltas para cada um de 5 corredores. Escreva um programa que leia o nome do corredor e todos os seus tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor e os valores são os tempos armazenados na forma de lista. Veja o exemplo:

# {
#   'João':   [77.0, 77.3, 73.9, 77.1, 75.9],
#   'Maria':  [79.2, 78.0, 78.5, 73.5, 78.9],
#   'Pedro':  [79.1, 75.8, 76.5, 73.5, 79.2],
#   'Ana':    [73.4, 75.2, 78.9, 76.5, 73.0],
#   'Carlos': [74.5, 79.1, 73.2, 76.6, 73.5]
# }
# Ao final mostre classificação final em ordem (primeiro o vencedor(a)), como mostrado a seguir:

# -------|------------------|-------------|-------------|--------------
#  Ordem | Nome do Corredor | Tempo Total | Tempo Médio | Melhor Volta 
# -------|------------------|-------------|-------------|--------------
#    1   |      Carlos      |    376.9    |    75.4     |     73.2     
#    2   |       Ana        |    377.0    |    75.4     |     73.0     
#    3   |       João       |    381.2    |    76.2     |     73.9     
#    4   |      Pedro       |    384.1    |    76.8     |     73.5     
#    5   |      Maria       |    388.1    |    77.6     |     73.5     
# -------|------------------|-------------|-------------|--------------
# Sugestões
# 1) Sempre arredonde todos os cálculos para 1 (uma) casa decimal;

# 2) Use o operador ^ dentro de uma f-string para centralizar o texto dentro de uma coluna. Por exemplo, print(f’{ordem:^7}’) coloca o texto centralizado em um campo de 7 caracteres de largura;

# 3) Crie uma estrutura de dados auxiliar (lista, tupla ou dicionário) para guardar a classificação;

# (
#     ('Carlos', 376.9, 75.4, 73.2), 
#     ('Ana', 377.0, 75.4, 73.0), 
#     ('João', 381.2, 76.2, 73.9), 
#     ('Pedro', 384.1, 76.8, 73.5), 
#     ('Maria', 388.1, 77.6, 73.5)
# )
# 4) Use itemgetter do pacote operator para fazer a ordenação da classificação.

# from operator import itemgetter
# ...
# resultado.sort(key=itemgetter(1))

from operator import itemgetter

def corrida():
    tempos_corredores = {}
    for _ in range(5):
        nome_corredor = str(input().strip())
        tempos = []
        for volta in range(1, 6):
            tempo = float(input())
            tempos.append(tempo)
        tempos_corredores[nome_corredor] = tempos
    classificacao = []
    for corredor, tempos in tempos_corredores.items():
        tempo_total = round(sum(tempos), 1)
        tempo_medio = round(sum(tempos) / len(tempos), 1)
        melhor_volta = round(min(tempos), 1)
        classificacao.append((corredor, tempo_total, tempo_medio, melhor_volta))
    classificacao.sort(key=itemgetter(1))
    return classificacao




def main():
    classificacao = corrida()
    print("-------|------------------|-------------|-------------|--------------")
    print(f"{'Ordem':^7}|{'Nome do Corredor':^18}|{'Tempo Total':^13}|{'Tempo Médio':^13}|{'Melhor Volta':^14}")
    print("-------|------------------|-------------|-------------|--------------")
    for ordem, (corredor, tempo_total, tempo_medio, melhor_volta) in enumerate(classificacao, start=1):
        print(f"{ordem:^7}|{corredor:^18}|{tempo_total:^13}|{tempo_medio:^13}|{melhor_volta:^14}")    
    print("-------|------------------|-------------|-------------|--------------")



if __name__ =='__main__':
	main()