"""

17) Escreva um programa que, dada uma lista de listas (matriz), retorne outra matriz que seja a
transposta da original.
**Exemplo:** `matriz = [[1, 2, 3], [4, 5, 6]]` -> `[[1, 4], [2, 5], [3, 6]]`

"""

def transporMatriz(matriz):
    transposta = []
    for x in range(len(matriz[0])):
        linha = []
        for y in range(len(matriz)):
            linha.append(matriz[y][x])
        transposta.append(linha)
    return transposta

def main():
    matriz = []
    while True:
        linha = []
        while True:
            try:
                num = input("Digite um número para a linha ou 'sair' para finalizar: ")
                if num == "sair":
                    break
                linha.append(int(num))
            except ValueError:
                print("Entrada inválida! Digite um número.")
        if not linha:
            break
        matriz.append(linha)
    if len(matriz)>0:
        print(transporMatriz(matriz))
    else:
        print("A matriz não foi criada!")

if __name__ == "__main__":
    main()