def main():
                nome = str(input("Digite seu nome:").strip())
                sexo = int(input("Digite seu sua opção sexual: número 1 para masculino e 2 para feminino."))
                if(sexo==1):
                                print(f'Ilmo Sr. {nome}')
                else:
                                print(f'Ilma Sra. {nome}')



if __name__ == '__main__':
    main()