'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa que leia um número e determine se ele é ou não primo.
'''



def conferirNumeroPrimo(n):
    primo = True
    if n <= 1:
        primo = False
    else:
        i = 2
        while i <= n**0.5:
            if n % i == 0:
                primo = False
                break
            else:
                i += 1
    if primo:
        return f"sim"
    else:
        return f"não"



def main():
    n = int(input("Digite um número: "))
    primo = conferirNumeroPrimo(n)
    print(f"O número {n}, {primo} é primo.")




if __name__ == '__main__':
    main()