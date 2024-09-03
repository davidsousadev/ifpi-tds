# Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos.
def alunosAbaixoDaMedia(nomes, idades, alturas, media_altura):
    lista = []
    for i in range(30):
        if idades[i] > 13 and alturas[i] < round(media_altura, 2):
            lista.append((nomes[i], idades[i], alturas[i]))
    return lista
def inserirItens(nomes, idades, alturas):
    for i in range(30):
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        altura = float(input("Digite a altura do aluno: "))
        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
    return nomes, idades, alturas

def main():

    nomes = []
    idades = []
    alturas = []
    nomes, idades, alturas = inserirItens(nomes, idades, alturas)   
    
    media_altura = sum(alturas) / len(alturas)
    
    alunos_13_anos_abaixo_media = alunosAbaixoDaMedia(nomes, idades, alturas, media_altura)
    print(f"MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for aluno in alunos_13_anos_abaixo_media:
        print(aluno[0])

if __name__ == '__main__':
    main()