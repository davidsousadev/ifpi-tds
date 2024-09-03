#Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5. DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

def multiplica(lista_ordenada):
    for i in range(len(lista_ordenada)):
        if i % 2 == 0:
            lista_ordenada[i] *= 3
        else:
            lista_ordenada[i]*= 5
    return lista_ordenada

def inserirItens():
    lista = []
    for i in range(100):
        lista.append(int(input("Digite um valor: ")))
    return lista
def main():
    lista_numeros = inserirItens()

    lista_ordenada = sorted(lista_numeros)
    nova_lista = multiplica(lista_ordenada)

    print(f"Essa e a lista ordenada e multiplicada: {nova_lista}")

if __name__ == "__main__":
    main()
