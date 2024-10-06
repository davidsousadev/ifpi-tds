from random import *



def main():
    animais = {
        'gato': {
            'macho': ["xanin", "garfild", "juarez"],
            'femea': ["cleopatra", "aila", "leoa"],
            'outro': ["ester", "lili", "esmeralda"]
        },
        'cachorro': {
            'macho': ["ralf", "caramelo", "cleitin"],
            'femea': ["princesa", "minerva", "polli"],
            'outro': ["leo", "romeu", "espiro"]
        }     
    }
    print("Serviço de escolha de nome para animais de estimação")
    print("-------------------")
    qtd = int(input("Qual a quantidade de animais? "))
    for i in range(qtd):
        tipo = input("Digite o tipo do animal: gato ou cachorro ").lower()
        if tipo in animais:
            genero = input("Digite o gênero do animal: macho/femea/outro ").lower()
            if genero in animais[tipo]:
                escolha = choice(animais[tipo][genero])
                print(f"Você deve chamar seu animal de estimação de {escolha}")
                animais[tipo][genero].remove(escolha)
            else:
                print("Não tem mais nomes.")
        else:
            print("Não tem mais nomes.")



if __name__ == '__main__':
    main()