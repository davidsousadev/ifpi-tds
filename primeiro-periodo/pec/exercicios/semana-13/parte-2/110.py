# Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso. IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:
# esta_ordenado([1, 2, 2]) True
# esta_ordenado(['b', 'a']) False



def inserirElementos(n, lista):
    for i in range(n):
        x = input("Digite os itens da lista: ").strip()
        try:
            x = float(x)
        except ValueError:
            pass
        lista.append(x)
    return lista



def main():
    n = int(input("Digite a quantidade de itens: "))
    lista = []
    lista = inserirElementos(n, lista)
    if sorted(lista) == lista:
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")




if __name__ == "__main__":
    main()