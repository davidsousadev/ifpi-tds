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