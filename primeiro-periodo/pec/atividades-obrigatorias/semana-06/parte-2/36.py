'''Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa frase sem considerar espaços em branco no início ou final da frase digitada.'''
def main():
    s = str(input("Digite uma frase ou palavra:").strip())
    quantidadecaractere = len(s)
    print(f'Esta frase ou palavra tem {quantidadecaractere} caracteres.')

if __name__ == '__main__':
    main()
    