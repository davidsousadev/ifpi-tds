# Crie um programa que cadastre informações de 20 pessoas (nome, idade e cpf) e coloque em um dicionário. Após a leitura, remova todas as pessoas menores de 18 anos do dicionário e coloque-as separadas em outro dicionário. Imprima os dois dicionários separando os campos por ; (ponto-e-vírgula).

def cadastrar_pessoa():
    pessoas = {}
    for i in range(20):
        nome = str(input().strip())
        idade = int(input())
        cpf = str(input().strip())
        pessoas[i + 1] = {"nome": nome, "idade": idade, "cpf": cpf}

    menores_de_18 = {}
    chaves_a_remover = []

    for chave, valor in pessoas.items():
        if valor["idade"] < 18:
            menores_de_18[chave] = valor
            chaves_a_remover.append(chave)

    for chave in chaves_a_remover:
        del pessoas[chave]
    return pessoas, menores_de_18



def main():
    
    pessoas, menores_de_18 = cadastrar_pessoa()
    print("========== MAIORES DE 18 ANOS ==========")
    for pessoa in pessoas.values():
        print(f"{pessoa['nome']};{pessoa['idade']};{pessoa['cpf']}")

    print("========== MENORES DE 18 ANOS ==========")
    for pessoa in menores_de_18.values():
        print(f"{pessoa['nome']};{pessoa['idade']};{pessoa['cpf']}")




if __name__ =='__main__':
	main()