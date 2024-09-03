def verificar_par(n):
    par = 0
    if 100 <= n <= 999:
        u = n % 100
        n = n // 10
        d = n % 10
        n = n // 10
        c = n % 10
        if c % 2 == 0:
            par += 1
        if d % 2 == 0:
            par += 1
        if u % 2 == 0:
            par += 1
        else:
            return 0
    return par


def main():
    n = int(input("Digite um número inteiro entre 100 e 999: "))
    par = verificar_par(n)
    print(f'Esse número tem {par} números pares.')



if __name__ == '__main__':
    main()
