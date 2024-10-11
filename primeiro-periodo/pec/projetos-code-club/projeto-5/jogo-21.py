from random import *
score = 0
print('''
Vinte e um!
=========
Tente fazer exatamente 21 pontos!

''')

while score < 21:
    numero = randint(1,10)
    score += numero
    print("\nSeu próximo número é ", numero)
    print("Sua pontuação agora é ", score)

    print("\nGostaria de somar mais um número? (s/n)")
    resposta = input().lower()
    if resposta == 'n' or resposta == 'nao':
        break


print("\nSua pontuação final é", score)
if score == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!!")