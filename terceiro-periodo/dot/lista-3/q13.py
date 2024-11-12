"""

13) Escreva uma função `rotacionar_lista(lista, n)` que rotacione os elementos de uma lista `n`
vezes para a direita.
**Exemplo:** `rotacionar_lista([1, 2, 3, 4, 5], 2)` -> `[4, 5, 1, 2, 3]`

"""

def rotacionar_lista(lista, n):
    
    n = n % len(lista)
    parte1 = lista[-n:]
    parte2 = lista[:-n]
    return parte1 + parte2

def main():
    lista = []
    while True:
        try:
            num = input("Digite uma nota para lista1 ou 'sair' para finalizar: ")
            if num == "sair":
                if len(lista) > 0:
                    break
                
            lista.append(int(num))
            
        except ValueError:
            print("Entrada inválida! Digite um número.")

    while True:
        try:
            n = int(input("Digite o número de rotações: "))
            if len(lista) > 0:
                
                print(rotacionar_lista(lista, n))
                
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    

if __name__ == "__main__":
    main()