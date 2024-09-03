def quantidade_de_pares_ou_impares(n):
    if 10 <= n <= 99:
        par = 0
        impar = 0
        u = n % 100
        n = n // 10
        d = n % 10
        if d % 2 == 0:
            par += 1
        if u % 2 == 0:
            par += 1
        if d % 2 != 0:
            impar += 1
        if u % 2 != 0:
            impar += 1
        if impar == 0:
            return "Nenhum dígito é ímpar."
        if impar == 1:
            return "Apenas um dígito é ímpar."
        if impar == 2:
            return "Os dois dígitos são ímpares."
    else:
        return "Numero invalido"


def main():
    n = int(input("Digite um número inteiro entre 10 e 99: "))
    msg = quantidade_de_pares_ou_impares(n)
    print(f'{msg}')



if __name__ == '__main__':
    main()
