"""

10) Crie uma lista `notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]` e escreva um programa que
identifique a nota mais alta e a nota mais baixa da lista sem usar as funções `max` e `min`.
Exiba ambas ao final.

"""

def maiorEMenorNota(notas):
    maior = notas[0]
    menor = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    return maior, menor

def main():
    notas = []
    while True:
        try:
            num = input("Digite uma nota ou 'sair' para finalizar: ")
            if num == "sair":
                if notas:
                    maior, menor = maiorEMenorNota(notas)
                    print("Nota mais alta:", maior)
                    print("Nota mais baixa:", menor)
                    break
                else:
                    print("Nenhuma nota foi inserida.") 
            notas.append(float(num))
        except ValueError:
            print("Entrada inválida! Digite um número.")
    

if __name__ == "__main__":
    main()
