def main():
    score = 0
    print('''
    Q1 - Qual a minha idade?
    a - 22 anos
    b - 27 anos
    c - 18 anos
    ''')
    respostas = input().lower()
    if respostas == "a":
        print("Não é a resposta passou muito perto :( ")
    elif respostas == "b":
        print(" Correto!! :) ")
        score = score + 1
    elif respostas == "c":
        print(" Não seja bobinho! :( ")
    else:
        print("Você não escolheu a, b ou c :( ")

    print('''
    Q2 - Qual a minha comida favorita?
    a - Lasanha
    b - Salada
    c - Pizza
    ''')
    respostas = input().lower()
    if respostas == "a":
        print(" Correto!! :) ")
        score = score + 1
    elif respostas == "b":
        print(" Não seja bobinho! :( ")
    elif respostas == "c":
        print("Não é a resposta passou muito perto :( ")
    else:
        print("Você não escolheu a, b ou c :( ")

    print('''
    Q3 - Qual a minha materia favorita?
    a - Filosofia
    b - Quimica
    c - Matematica
    ''')
    respostas = input().lower()
    if respostas == "a":
        print(" Não seja bobinho! :( ")
    elif respostas == "b":
        print("Não é a resposta passou muito perto :( ")
    elif respostas == "c":
        print(" Correto!! :) ")
        score = score + 1
    else:
        print("Você não escolheu a, b ou c :( ")

    print('''
    Q4 - Qual meu esporte favorito?
    a - Volei
    b - Futebol
    c - Basquete
    ''')
    respostas = input().lower()
    if respostas == "a":
        print(" Não seja bobinho! :( ")
    elif respostas == "b":
        print(" Correto!! :) ")
        score = score + 1
    elif respostas == "c":
        print("Não é a resposta passou muito perto :( ")
    else:
        print("Você não escolheu a, b ou c :( ")

    print('''
    Q5 - Que tipo de musica eu mais gosto?
    a - Gospel
    b - Pop
    c - Rock
    ''')
    respostas = input().lower()
    if respostas == "a":
        print(" Correto!! :) ")
        score = score + 1
    elif respostas == "b":
        print("Não é a resposta passou muito perto :( ")
    elif respostas == "c":
        print(" Não seja bobinho! :( ")
    else:
        print("Você não escolheu a, b ou c :( ")
    print("Pontuação:", score)
    if(score==5):
        print("muito bem!")
    else:
        print("tente novamente")

if __name__ == '__main__':
    main()
