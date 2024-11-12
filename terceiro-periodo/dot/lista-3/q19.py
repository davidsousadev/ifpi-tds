"""

19) Dada uma lista de números, escreva um programa que retorne todos os pares de elementos que
somam um valor específico `k`.
**Exemplo:** Para `lista = [1, 2, 3, 4, 5]` e `k = 6`, o programa deve retornar `[(1, 5), (2, 4)]`.

"""


def somaParesdek(lista, k):
    resultado = []
    for x in range(len(lista)):
        for y in range(x + 1, len(lista)):
            if lista[x] + lista[y] == k:
                resultado.append((lista[x], lista[y]))
                
    if not len(resultado)>0:
        resultado = "Nenhum"
    
    return resultado
        

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

    while True:
        try:
            k = int(input("Digite o valor de k: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

    print(f"Pares que somam {k}: {somaParesdek(lista, k)}")

if __name__ == "__main__":
    main()