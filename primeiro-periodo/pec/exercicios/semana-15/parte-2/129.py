# A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em mil unidades.

# Fabricante / Ano	2013	2014	2015	2016	2017	2018
# Fiat	204	223	230	257	290	322
# Ford	195	192	198	203	208	228
# GM	220	222	217	231	245	280
# Wolkswagen	254	262	270	284	296	330
# Faça um programa que:

# leia os dados da tabela pelo teclado;
# leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
# determine e exiba o ano de maior volume geral de vendas.
# determine e exiba a média anual de vendas de cada fabricante durante o período.

def ler_dados():
    fabricantes = ["Fiat", "Ford", "GM", "Wolkswagen"]
    dados = {}

    for fabricante in fabricantes:
        vendas = [int(input(f"Digite a quantidade de vendas do fabricante {fabricante} no ano {ano}: ")) for ano in range(2013, 2019)]
        dados[fabricante] = vendas

    return dados

def fabricante_mais_vendeu_ano(dados, ano):
    vendas_ano = {fabricante: dados[fabricante][ano - 2013] for fabricante in dados}
    fabricante_mais_vendido = max(vendas_ano, key=vendas_ano.get)
    quantidade_vendida = vendas_ano[fabricante_mais_vendido]
    return fabricante_mais_vendido, quantidade_vendida

def ano_maior_volume_vendas(dados):
    total_anual = {ano: sum(dados[fabricante][ano - 2013] for fabricante in dados) for ano in range(2013, 2019)}
    ano_maior_volume = max(total_anual, key=total_anual.get)
    volume_maior_ano = total_anual[ano_maior_volume]
    return ano_maior_volume, volume_maior_ano

def media_anual_vendas(dados):
    medias = {fabricante: sum(dados[fabricante]) / len(dados[fabricante]) for fabricante in dados}
    return medias

def main():
    dados = ler_dados()
    ano_escolhido = int(input("Digite um ano entre 2013 e 2019: "))
    fabricante_mais_vendido, quantidade_vendida = fabricante_mais_vendeu_ano(dados, ano_escolhido)
    print(f"A fabricante que mais vendeu em {ano_escolhido} foi a {fabricante_mais_vendido} com {quantidade_vendida} mil unidades.")

    ano_maior_volume, volume_maior_ano = ano_maior_volume_vendas(dados)
    print(f"O ano de maior volume geral de vendas foi {ano_maior_volume} com {round(volume_maior_ano, 2)} mil unidades.")

    medias = media_anual_vendas(dados)
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    for fabricante, media in medias.items():
        print(f"A {fabricante} vendeu em média {round(media,2)} unidades por ano.")

if __name__ == "__main__":
    main()
