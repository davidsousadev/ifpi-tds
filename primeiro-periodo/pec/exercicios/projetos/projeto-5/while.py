from random import *
jogador = True
score = 0
print('''
Porta da fortuna!
=========

Existe um super prémio atrás de uma dessas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio
    _____   _____   _____
   |     | |     | |     |
   | [1] | | [2] | | [3] |
   |   ° | |   ° | |   ° |
   |_____| |_____| |_____|
''')

while jogador == True:
    print("\nEscolha uma porta (1, 2 ou 3):")
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1,3)
    print("A porta escolhida foia a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida== portaCerta:
        print("Parabéns!")
        score +=1
    else:
        score = 0
        print("Que peninha!")
    
    print(f"Sua pontuação é", score)

    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()
    if resposta == 'n' or resposta == 'nao':
        jogador= False


print("Obrigado por jogar.")
print("Sua pontuação final é de", score)
