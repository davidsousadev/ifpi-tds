# Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do maior e menor elemento.



def maiorEMenor(tupla):
    maior = menor = tupla[0][0]
    posicaoMaior = posicaoMenor = (0, 0)
    for i in range(len(tupla)):
        for j in range(len(tupla[i])):
            if tupla[i][j] > maior:
                maior = tupla[i][j]
                posicaoMaior = (i, j)
            elif tupla[i][j] < menor:
                menor = tupla[i][j]
                posicaoMenor = (i, j)
    return posicaoMaior, posicaoMenor 



def inserirDados(qtd):
    tupla = []
    for i in range(qtd):
        lista = []
        for j in range(qtd):
            elemento = float(input(f"Digite o elemento para linha {i+1} e coluna {j+1}: "))
            lista.append(elemento)
        tupla.append(lista)
    return tupla



def main():

    qtd = int(input("Digite a quantidade de linhas e colunas da matriz quadratica: "))
    tupla = inserirDados(qtd)
    posicaoMaior, posicaoMenor = maiorEMenor(tupla)
    print(f"Esse e o maior elemento e sua posição {posicaoMaior}\nEssse e o menor elemento e sua posição {posicaoMenor}")



if __name__=='__main__':
    main()