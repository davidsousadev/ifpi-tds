from random import *



def main():
    print("Gerador de Cumprimentos")
    print("-------------------")
    adjetivos = ["maravilhoso", "acima da média", "excelente", "lindo"] 
    hobbies = ["andar de bicicleta", "programar", "fazer chá", "jogar video game"] 
    nome = input("Qual é o seu nome?: ") 
    print("Aqui está o seu cumprimento, " + nome + ":")
    print(nome + ", você é " + choice(adjetivos) + " em " + choice(hobbies))
    print("De nada!")




if __name__ == '__main__':
    main()