def main():  
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    #chave = 3

    num = int(input("Digite a chave (numero inteiro): "))
    letra = input("Por favor, entre com uma letra para criptografar: ")
    posisao = alfabeto.find(letra)
    novaPosisao = (posisao + num) % 26
    letraCriptografada = alfabeto[novaPosisao]
    print("Sua letra criptografada e: " + letraCriptografada)
if __name__ == "__main__":
    main()
