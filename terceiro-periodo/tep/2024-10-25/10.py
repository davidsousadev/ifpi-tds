"""

10) Considere o conjunto de informações abaixo:
dados = {
'Crossfox': {'km': 35000, 'ano': 2005},
'DS5': {'km': 17000, 'ano': 2015},
'Fusca': {'km': 130000, 'ano': 1979},
'Jetta': {'km': 56000, 'ano': 2011},
'Passat': {'km': 62000, 'ano': 1999}
}
Km_media = km_total/(ano_atual – ano_fabricação)
Complete o corpo da função:
def km_media(dataset,ano_atual):
...
a função acima obtém e imprime a quilometragem média anual de cada veículo em um dicionário
com a estrutura do dicionário “dados” acima:
Ex. de chamada da função:
km_media(dados, 2019)
Saída:

"""


dados = {
'Crossfox': {'km': 35000, 'ano': 2005},
'DS5': {'km': 17000, 'ano': 2015},
'Fusca': {'km': 130000, 'ano': 1979},
'Jetta': {'km': 56000, 'ano': 2011},
'Passat': {'km': 62000, 'ano': 1999}
}



def km_media(dados, ano_atual):
    for dado in dados.items():
        if dado[1]["ano"] <= ano_atual:
            
            km_media = (dado[1]["km"] / (ano_atual - dado[1]["ano"]))
            print(km_media)


km_media(dados, 2019)