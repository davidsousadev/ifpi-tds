'''
Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.
'''
def par_impar():
    par = 0
    impar = 0
    for i in range(1,101):
        x = int(input())
        if(x%2==0):
            par += 1
        else:
            impar +=1
    return par, impar



def main():
    par, impar = par_impar()
    print(par)
    print(impar)



if __name__ == '__main__':
    main()