"""

16) Escreva uma função `agrupa_por_paridade(lista)` que divida uma lista de números em duas
listas: uma contendo os números pares e outra os ímpares, e retorne uma lista contendo ambas
as listas.
**Exemplo:** `lista = [1, 2, 3, 4, 5, 6]` -> `[[2, 4, 6], [1, 3, 5]]`


"""

def agrupaPorParidade(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return [pares, impares]

def main():
    lista = []
    while True:
        try:
            num = input("Digite um número para a lista ou 'sair' para finalizar: ")
            if num.lower() == "sair":
                break
            lista.append(int(num))
            
        except ValueError:
            print("Entrada inválida! Digite um número.")

    print(agrupaPorParidade(lista))

if __name__ == "__main__":
    main()