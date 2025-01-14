"""

Pesquise na internet sobre manipulação de arquivos .CSV com python
A seguir, escolha um dataset disponível no classroom e implemente classes (1:N) que representem este dataset. Implemente um método para leitura desses dados e produza pelo menos 2 relatórios (criar 2 métodos)

Ex: Lista dos países que não consomem bebidas alcoolicas, qual a bebida mais consumida? Qual o país com maior consumo de vinho? 
atentados terorristas com maior numero de mortes, etc

"""

import csv

class Pais:
    def __init__(self, country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol):
        self.country = country
        self.beer_servings = beer_servings
        self.spirit_servings = spirit_servings
        self.wine_servings = wine_servings
        self.total_litres_of_pure_alcohol = total_litres_of_pure_alcohol

class Relatorio:
    def __init__(self, paises):
        self.paises = paises

    @classmethod
    def ler_dados(cls, arquivo_csv):
        paises = []
        with open(arquivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                pais = Pais(
                    country=linha['country'],
                    beer_servings=float(linha['beer_servings']),
                    spirit_servings=float(linha['spirit_servings']),
                    wine_servings=float(linha['wine_servings']),
                    total_litres_of_pure_alcohol=float(linha['total_litres_of_pure_alcohol'])
                )
                paises.append(pais)
        return cls(paises)

    def paises_sem_consumo_alcool(self):
        sem_alcool = []
        for pais in self.paises:
            if pais.total_litres_of_pure_alcohol == 0:
                sem_alcool.append(pais.country)

        resultado = "Países sem Consumo de Álcool:\n"
        for pais in sem_alcool:
            resultado += f"{pais}\n"
        return resultado.strip()

    def pais_maior_consumo_vinho(self):
        maior_vinho = None
        for pais in self.paises:
            if maior_vinho is None:
                maior_vinho = pais
            elif pais.wine_servings > maior_vinho.wine_servings:
                maior_vinho = pais

        resultado = f"País com maior consumo de vinho: {maior_vinho.country} ({maior_vinho.wine_servings} servings)\n"
        return resultado

    def pais_maior_consumo_alcool_total(self):
        maior_alcool = None
        for pais in self.paises:
            if maior_alcool is None:
                maior_alcool = pais
            elif pais.total_litres_of_pure_alcohol > maior_alcool.total_litres_of_pure_alcohol:
                maior_alcool = pais

        resultado = f"País com maior consumo total de álcool: {maior_alcool.country} ({maior_alcool.total_litres_of_pure_alcohol} litros)\n"
        return resultado
def main():
    relatorio = Relatorio.ler_dados('drinks.csv')
    print(relatorio.paises_sem_consumo_alcool())
    print(relatorio.pais_maior_consumo_vinho())
    print(relatorio.pais_maior_consumo_alcool_total())

if __name__=="__main__":
    main()