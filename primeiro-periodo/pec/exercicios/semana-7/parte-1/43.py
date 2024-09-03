def main():
                sinal = str(input("Qual a cor do sinal: (“V” é verde; “A” é amarelo; “E” é vermelho)\n").strip())
                print("O sinal indica que: ")
                if(sinal=="V" or sinal=="v"):
                                print("Siga")
                elif(sinal=="A" or sinal=="a"):
                                print("Atenção")
                elif(sinal=="E" or sinal=="e"):
                                print("Pare")




if __name__ == '__main__':
    main()