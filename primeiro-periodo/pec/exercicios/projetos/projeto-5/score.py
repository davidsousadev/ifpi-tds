from random import *

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
score = 0
for attempt in range(3):
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
        print("Que peninha!")
print(f"A pontuação foi: {score}")