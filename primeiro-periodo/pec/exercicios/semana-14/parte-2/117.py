# Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de
# números negativos e a soma dos números positivos dessa lista.



def calculaNegativosEPositivos(lista):
    negativos = 0
    soma = 0
    for num in lista:
        if num < 0:
            negativos += 1
        elif num > 0:
            soma += num
    return negativos, soma




def main():
    reais = []
    for x in range(10):
      num = int(input("Digite um numero: "))
      reais.append(num)
    print(reais)
    negativos, soma = calculaNegativosEPositivos(reais)
    print(f"Quantidade de numeros negativos :{negativos}")
    print(f"Soma dos numeros: {soma}")




if __name__ == '__main__':
    main()