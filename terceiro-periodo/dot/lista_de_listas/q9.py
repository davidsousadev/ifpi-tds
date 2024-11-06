"""

9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela 
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

"""




def main():
    max_itens = 5
    while True:
        listaX = []
        for x in range(max_itens):
            elemento = input("Digite um elemento: ").strip()
            listaX.append(elemento)
        listaY = listaX[::-1]
        print(listaY)
        
        break 
      
if __name__ == "__main__":
    main()