"""

11) Faça um programa que alimente uma lista com um número de posições definidas pelo 
usuário. 
Esta lista deverá armazenar um conjunto de nomes em diferentes posições. 
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente. 
======MENU======== 
1)Cadastar nome 
2)Pesquisar nome 
3)Listar todos os nome 
0) Sair do programa 
——————– 
Digite sua escolha:_ 

"""



def main():
    lista = []
    while True:
        print("=========MENU===========")
        print("1) Cadastar nome ")
        print("2) Pesquisar nome ")
        print("3) Listar todos os nome ")
        print("0) Sair do programa ")
        print("————————————————————————")
        try:
            opcao = int(input("Digite sua escolha: "))
        
            
            match opcao:
                case 1:
                    while True:
                        try:
                            nome = input("Digite um nome: ")
                            if nome.isalpha():
                                lista.append(nome)
                                print(f"{nome}\nAdicionado com sucesso!\n")
                                break
                            else:
                                raise ValueError("Entrada inválida! Digite um nome.")
                                                                                                  
                        except ValueError as e:
                            print(f"\n{e}\n")

                case 2:
                    while True:
                        try:
                            while True:
                                nome = input("Digite um nome para procurar: ").strip()
                                if nome in lista:
                                    print(f"{nome}\nLocalizado com sucesso!\n")
                                    break
                                elif nome not in lista:
                                    print(f"{nome}\nNão localizado com sucesso!\n")
                                else:
                                    raise ValueError("Entrada inválida! Digite um nome.")
                                                                                
                        except ValueError as e:
                            print(f"\n{e}\n")
                        break
                case 3:
                    if lista:
                        print("\nLista de Nomes:")
                        for x in range(len(lista)):
                            print(f"{x + 1}: {lista[x]}")
                        print("\n")
                    else:
                        print("\nA lista está vazia.\n")

                case 0:
                    print("Programa encerrado!")
                    break
                case _:
                    print("Entrada inválida! Digite uma opção valida.")

        except ValueError:
                print("Entrada inválida! Digite uma opção valida.")
        
         
      
if __name__ == "__main__":
    main()