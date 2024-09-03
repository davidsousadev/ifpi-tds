# Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.

# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o valor da constante e retorna uma nova lista com os elementos multiplicados.



def multiplica_constante(numeros, constante):
    consoantes = []
    for elemento in numeros:
        elementos = elemento * constante
        consoantes.append(elementos)
    return consoantes

def inserirItens(numeros):
    while True:
        numero = int(input("Digite um numero / Digite 0 para encerrar o loop!"))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def main():
    numeros = []

    numeros = inserirItens(numeros)

    constante = int(input("Digite o valor para multiplicar os itens: "))
    nova_lista = multiplica_constante(numeros, constante)
    print(f"Lista multiplicada: {nova_lista}")
    
    
    
if __name__ == "__main__":
    main()
