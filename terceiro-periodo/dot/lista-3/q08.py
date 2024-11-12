"""

8) Escreva um programa que receba duas listas de números de mesmo tamanho e retorne uma
nova lista onde cada elemento é a soma dos elementos nas mesmas posições nas listas originais.
Exemplo: se `lista1 = [1, 2, 3]` e `lista2 = [4, 5, 6]`, o código deve retornar `[5, 7, 9]`.

"""

def somar_listas(lista1, lista2):
    
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])
        
    return resultado

def main():
    lista1 = []
    lista2 = []
    
    while True:
        print("\nLista 1:")
        while True:
            try:
                num = int(input("Digite um número para lista 1 ou 0 para finalizar : "))
                if num == 0:
                    break
                lista1.append(num)
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
        
        print("\nLista 2:")
        while True:
            try:
                num = int(input("Digite um número para lista 2 ou 0 para finalizar: "))
                if num == 0:
                    break
                lista2.append(num)
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
        
        # Verifica o tamanho das listas
        if len(lista1) == len(lista2):
            print("As listas têm o mesmo tamanho.")
            print("Soma das listas:", somar_listas(lista1, lista2))
            break
        else:
            print("As listas ainda não têm o mesmo tamanho.")
            if len(lista1) > len(lista2):
                diferenca = len(lista1) - len(lista2)
                print(f"Adicione mais {diferenca} elemento a lista2.") 
            if len(lista1) < len(lista2):
                diferenca = len(lista2) - len(lista1)
                print(f"Adicione mais {diferenca} elemento a lista1.") 
            

if __name__ == "__main__":
    main()
