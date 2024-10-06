'''Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

'''

def mediaNotas(n1, n2, n3):
                media = (n1+n2+n3)/3
                if(n3>8):
                                media +=1              
                if(media>10):
                                media = 10
                return media





def main():                
                n1 = float(input("Digite a primeira nota: "))
                n2 = float(input("Digite a segunda nota: "))
                n3 = float(input("Digite a terceira nota: "))
                media = mediaNotas(n1,n2,n3)
                if(media == 10.00):              
                                print('%.0f'%media)
                else:
                                print('%.2f'%media)



if __name__ == '__main__':
    main()