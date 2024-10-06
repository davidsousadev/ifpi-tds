'''O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).'''

def calcular(dataDeNascimento):
    numeroDaSorte = 0
    while dataDeNascimento > 0: 
        unidade = dataDeNascimento % 10
        numeroDaSorte += unidade
        dataDeNascimento = dataDeNascimento // 10
    return numeroDaSorte



def main():
    dataDeNascimento = int(input("Digite a data de nascimento no formado ddmmaaaa (um número inteiro com 8 dígitos): "))
    numeroDaSorte = calcular(dataDeNascimento)
    print(f"Esse e o seu númeero da sorte {numeroDaSorte}.")




if __name__ == '__main__':
    main()