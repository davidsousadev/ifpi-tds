# Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura dos jogadores, determine: a. o nome e a altura do jogador mais alto; b. a média de altura do time; c. os jogadores com altura superior à média, listando o nome e a altura de cada um.
def inserirItens(nomes, alturas):
    for i in range(12):
        nome = input(f"Digite o nome do jogador {i+1}: ")
        altura = float(input(f"Digite a altura do jogador {i+1}: "))
        nomes.append(nome)
        alturas.append(altura)
    return nomes, alturas

def jodadorAcimaDaMedia(nomes,alturas,media_altura):
    jogadores_acima_media = []
    for i in range(12):
        if alturas[i] > media_altura:
            jogadores_acima_media.append((nomes[i], alturas[i]))
    return jogadores_acima_media

def main():
    nomes = []
    alturas = []
    nomes, alturas = inserirItens(nomes, alturas)
    
    indice_jogador_mais_alto = alturas.index(max(alturas))

    nome_mais_alto = nomes[indice_jogador_mais_alto]

    altura_mais_alto = alturas[indice_jogador_mais_alto]

    media_altura = sum(alturas) / len(alturas)
    
    jogadores_acima_media = []
    jogadores_acima_media = jodadorAcimaDaMedia(nomes, alturas, media_altura)
    print(f"JOGADOR MAIS ALTO DO TIME\n{nome_mais_alto}")
    print('%.2f' %altura_mais_alto)
    print(f"ALTURA MÉDIA DO TIME\n{round(media_altura,2)}")
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for jogador in jogadores_acima_media:
        print(f"{jogador[0]}")
        print('%.2f' %jogador[1])


if __name__ == '__main__':
    main()