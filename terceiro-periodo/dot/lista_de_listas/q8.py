"""

8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes 
ocorreu a letra 'A'.

"""


def verificaQuantidade(lista):
    quanrtidade_de_letras_a = 0
    for x in lista:
        if x=="A":
            quanrtidade_de_letras_a += 1
    return quanrtidade_de_letras_a

def main():
    max_itens = 2
    while True:
        lista = []
        for x in range(max_itens):
            while True:
                try:
                    letra = input("Digite uma letra: ").strip()
                    if letra.isalpha() and len(letra) == 1:
                        lista.append(letra)
                        break
                    else:
                        raise ValueError("Entrada inválida! Digite apenas uma letra.")
                except ValueError as e:
                    print(f"\n{e}\n")

        print(lista)
        print(f"A letra 'A' apareceu {verificaQuantidade(lista)} vezes.")
        break 
      
if __name__ == "__main__":
    main()