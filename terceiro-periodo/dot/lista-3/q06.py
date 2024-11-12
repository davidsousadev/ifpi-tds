"""

6) Escreva uma função `remover_duplicatas(lista)` que receba uma lista de números e retorne
uma nova lista sem elementos duplicados. Por exemplo, dado `[1, 2, 3, 1, 4, 2]`, a função deve
retornar `[1, 2, 3, 4]`.

"""


def remover_duplicatas(lista):
    
    resultado = []
    for num in lista:
        if num not in resultado:
            resultado.append(num)
            
    return resultado

def main():
    
    lista = []
    while True:
        try:
            num = input("Digite um elemento para lista ou 'sair' para finalizar: ")
            if num == "sair":
                break
            lista.append(int(num))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            
    print(remover_duplicatas(lista))

if __name__ == "__main__":
    main()