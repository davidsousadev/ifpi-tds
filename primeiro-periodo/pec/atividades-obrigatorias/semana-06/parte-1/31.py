'''Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.'''
def main():
    s = str(input("Digite um nome:").strip())
    print(f'Esse nome tem:',len(s),'caracteres.')
    
if __name__ == '__main__':
    main()