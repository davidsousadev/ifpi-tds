"""

7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um 
outro valor dado pertence ou não à lista. 

"""

def main():
    max_itens = 10
    while True:
        lista = []
        for x in range(max_itens):
            while True:
                try:
                    num = int(input(f"Digite um número an posição {x + 1 }: "))
                    lista.append(num)
                    break
                except ValueError:
                    print("\n Número invalido! \n")
                    
        while True:
            try:        
                num = int(input("Digite o valor para verificar se está na lista: "))
                if num in lista:
                    print(f"O número {num} está na lista.")
                else:
                    print(f"O número {num} não está na lista.")
                break
            except ValueError:
                print("\n Número invalido! \n")
                
        break 
      
if __name__ == "__main__":
    main()