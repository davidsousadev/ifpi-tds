"""

8) Considere o dicionário abaixo:
dados = {
'Crossfox': {'valor': 72000, 'ano': 2005},

'DS5': {'valor': 125000, 'ano': 2015},
'Fusca': {'valor': 150000, 'ano': 1976},
'Jetta': {'valor': 88000, 'ano': 2010},
'Passat': {'valor': 106000, 'ano': 1998}
}
Crie um trecho de código que imprime somente os nomes dos veículos com ano de fabricação maior
ou igual a 2000.

"""

dados = {
'Crossfox': {'valor': 72000, 'ano': 2005},
'DS5': {'valor': 125000, 'ano': 2015},
'Fusca': {'valor': 150000, 'ano': 1976},
'Jetta': {'valor': 88000, 'ano': 2010},
'Passat': {'valor': 106000, 'ano': 1998}
}


for dado in dados.items():
    if dado[1]["ano"] >= 2000:
        print(dado[0])