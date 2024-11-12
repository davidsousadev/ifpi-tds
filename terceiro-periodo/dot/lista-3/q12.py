"""

12) Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas
os números que são a soma de dois outros números distintos na mesma lista.
**Exemplo:** `lista = [3, 5, 7, 10, 15]` -> `[10, 15]` (pois 10 = 3 + 7 e 15 = 5 + 10)

"""

def somaDeDestintos(lista):
    resultado = []
    for num in lista:
        for x in range(len(lista)):
            for y in range(x + 1, len(lista)):
                if lista[x] + lista[y] == num and num not in resultado:
                    resultado.append(num)
    return resultado

def main():
    lista = []
    while True:
        try:
            num = input("Digite um número ou 'sair' para finalizar: ")
            if num == "sair":
                break
            lista.append(int(num))
        except ValueError:
            print("Entrada inválida! Digite um número.")
    print(somaDeDestintos(lista))

if __name__ == "__main__":
    main()