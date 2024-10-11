'''
Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:

521 = cinco centenas, duas dezenas e uma unidade.
107 = uma centena e sete unidades.
80 = oito dezenas.
'''
def numero_por_extenso(numero):
    quantidade = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    extenso = ""
    if 1 <= numero <= 999:
        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = numero % 10
        if centena > 0:
            extenso += f"{quantidade[centena]} centena{'s' if centena > 1 else ''}"
            extenso += f"{' e ' if dezena==0 and unidade > 0 else ''}"
        if dezena > 0:
            if centena > 0 and unidade > 0:
                extenso += ", "
            elif centena > 0:
                extenso += " e "
            if dezena == 1:
                extenso += f"{quantidade[dezena]} dezena{' e ' if unidade > 0 else ''}"
            else:
                extenso += f"{quantidade[dezena]} dezenas{' e ' if unidade > 0 else ''}"
        if unidade == 1:
            extenso += f"{quantidade[unidade]} unidade"
        elif unidade > 0:
            extenso += f"{quantidade[unidade]} unidades"
    return extenso



def main():
    numero = int(input("Digite um número entre 1 e 1000: "))
    extenso = numero_por_extenso(numero)
    print(f"Esse número tem : {extenso}.")



if __name__ == '__main__':
    main()