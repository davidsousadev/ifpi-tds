"""

14) Escreva um programa que receba uma lista de listas (matriz) e calcule a soma de todos os
elementos em cada linha, retornando uma nova lista com essas somas.
**Exemplo:** `matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `[6, 15, 24]`

"""

def somaLinhasMatriz(matriz):
    somas = []
    for linha in matriz:
        soma = 0
        for elemento in linha:
            soma += elemento
        somas.append(soma)
    return somas

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
        
    print(matriz)
    print(somaLinhasMatriz(matriz))

if __name__ == "__main__":
    main()

