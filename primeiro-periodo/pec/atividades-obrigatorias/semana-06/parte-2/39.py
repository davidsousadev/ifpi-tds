'''Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.

'''

def main():
    idade = int(input("Digite a idade de Zob em anos terrestes: "))
    idade = (idade//2)
    print(f'Esta e a idade de Zob em anos espaciais: {idade}')



if __name__ == '__main__':
    main()