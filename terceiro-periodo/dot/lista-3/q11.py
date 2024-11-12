"""

11) Escreva uma função intercalar_listas(lista1, lista2) que receba duas listas de qualquer
tamanho e retorne uma nova lista contendo os elementos intercalados de ambas. Se uma lista
for maior, adicione os elementos restantes ao final da nova lista.
**Exemplo:** `lista1 = [1, 3, 5]`, `lista2 = [2, 4, 6, 8, 10]` -> `[1, 2, 3, 4, 5, 6, 8, 10]`

"""

def intercalar_listas(lista1, lista2):
    resultado = []
    for x in range(max(len(lista1), len(lista2))):
        if x < len(lista1):
            resultado.append(lista1[x])
        if x < len(lista2):
            resultado.append(lista2[x])
    return resultado

def main():
    lista1 = []
    lista2 = []
    print("\nLista 1:")
    while True:
        try:
            num = input("Digite uma nota para lista1 ou 'sair' para finalizar: ")
            if num == "sair":
                break
            lista1.append(int(num))
        except ValueError:
            print("Entrada inválida! Digite um número.")
    print("\nLista 2:")
    while True:
        try:
            num = input("Digite uma nota para lista2 ou 'sair' para finalizar: ")
            if num == "sair":
                break
            lista2.append(int(num))
        except ValueError:
            print("Entrada inválida! Digite um número.")

    print(intercalar_listas(lista1, lista2))

if __name__ == "__main__":
    main()