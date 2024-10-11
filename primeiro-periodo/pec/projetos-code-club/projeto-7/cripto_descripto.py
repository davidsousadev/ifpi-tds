def cripto(texto, num, modo):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            if modo == 'cripto':
                novaPosicao = (posicao + num) % 26
            else:
                novaPosicao = (posicao - num) % 26
            resultado += alfabeto[novaPosicao]
        else:
            resultado += letra

    return resultado

def main():
    cripto_d = cripto('d', 7, 'cripto')
    cripto_x = cripto('x', 4, 'cripto')

    print(f"Letra 'd' criptografada com chave 7: {cripto_d}")
    print(f"Letra 'x' criptografada com chave 4: {cripto_x}")

    desemcriptar = cripto('omqemd', 12, '')
    print(f"Mensagem descriptografada: {desemcriptar}")

if __name__ == "__main__":
    main()