'''Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).'''

def transforma(s):
    h = s // 3600
    s = s % 3600
    min = s // 60
    s = s % 60
    return h, min, s

def main():
    s = int(input("Digite a quantidade de segundos:"))
    h, min, s = transforma(s)
    print(f'Esse e o valor convertido em horas : minutos : segundos')
    print(f'{h}:{min}:{s}')

if __name__ == '__main__':
    main()