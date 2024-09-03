def main():
                s = str(input("Digite um caractere: "))
                print("Esse caractere é: ")
                if(s in 'AEIOUaeiou' and s !=''):
                                print('vogal')
                elif('a' <= s <= 'z' or 'A' <= s <= 'Z'):
                                print('consoante')
                elif('0' <= s <= '9'):
                                print('número')
                else:
                                print('símbolo')



if __name__ == '__main__':
    main()