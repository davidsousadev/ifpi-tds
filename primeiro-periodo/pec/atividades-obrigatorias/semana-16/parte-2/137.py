# Escreva um programa que leia um texto e calcula a frequência relativa de cada letra no texto. Desconsidere a diferença entre maiúsculas e minúsculas mas considere caracteres acentuados. Por exemplo, para a frase: Se, a princípio, a ideia não é absurda, então não há esperança para ela. (Albert Einstein) Retorna o dicionário: {'S': 4, 'E': 10, 'A': 15, 'P': 4, 'R': 5, 'I': 7, 'N': 7, 'C': 2, 'O': 4, 'D': 2, 'B': 2, 'U': 1, 'T': 3, 'H': 1, 'L': 2}

from collections import Counter
import unicodedata

def calcular_frequencia_letras(texto):
    texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')).upper()
    contagem_letras = Counter(texto)
    contagem_letras = {letra: contagem_letras[letra] for letra in contagem_letras if letra.isalpha()}
    return contagem_letras



def main():
    texto = str(input().strip())
    resultados = calcular_frequencia_letras(texto)
    print(resultados)



if __name__ =='__main__':
	main()