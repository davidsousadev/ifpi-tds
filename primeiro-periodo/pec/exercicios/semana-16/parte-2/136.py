# Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada. Inclua as vogais com acentos na contagem.



def contar_vogais(texto):
    contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'á': 0, 'é': 0,'ê': 0, 'í': 0, 'ó': 0, 'ú': 0, 'ã': 0, 'õ': 0}

    texto = texto.lower()

    for char in texto:
        if char in contagem_vogais:
            contagem_vogais[char] += 1

    return contagem_vogais



def main():
    texto = str(input().strip())
    resultados = contar_vogais(texto)

    contagem_a = 0
    contagem_e = 0
    contagem_i = 0
    contagem_o = 0
    contagem_u = 0

    for vogal, contagem in resultados.items():
        if vogal=='á' or vogal=='ã' or vogal=='a':
            contagem_a += contagem
        if vogal=='e' or vogal=='é'or vogal=='ê':
            contagem_e += contagem
        if vogal=='i' or vogal=='í':
            contagem_i += contagem
        if vogal=='o' or vogal=='õ' or vogal=='ó':
            contagem_o += contagem
        if vogal=='u' or vogal=='ú':
            contagem_u += contagem

    print(f"A: {contagem_a}")
    print(f"E: {contagem_e}")
    print(f"I: {contagem_i}")
    print(f"O: {contagem_o}")
    print(f"U: {contagem_u}")



if __name__ =='__main__':
	main()