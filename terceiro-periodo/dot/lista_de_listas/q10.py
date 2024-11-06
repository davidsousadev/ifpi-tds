"""

10) Faça um programa que grave uma lista com 15 posições, calcule e mostre: 
a) O maior elemento da lista e em que posição esse elemento se encontra; 
b)    O menor elemento da lista e em que posição esse elemento se encontra.

"""

def maioreMenorElemento(lista):
    maior = lista[0]
    menor = lista[0]
    for x in lista:
        if x >= maior:
            maior = x
        elif x <= menor:
            menor = x
                 
    return maior, menor


def main():
    max_itens = 15
    while True:
        lista = []
        for x in range(max_itens):
            while True:
                try:
                    numero = int(input("Digite um número: "))
                    lista.append(numero)
                    break
                    
                except ValueError:
                    print("Entrada inválida! Digite um número.")

        maior, menor = maioreMenorElemento(lista)
        print(lista)
        print(f"Maior elemento da lista {maior}.")
        print(f"Menor elemento da lista {menor}.")
        
        break 
      
if __name__ == "__main__":
    main()