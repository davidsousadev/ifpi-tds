# Um entrevistador precisa saber o ano de nascimento em que 1000 (mil) pessoas e, no final, deseja saber a quantidade de pessoas que nasceram em cada ano. Crie um dicionário e, a cada valor lido, some 1 (um) na chave correspondente ao ano do dicionário. Mostre quantas pessoas nasceram em cada ano exibindo do mais antigo ao mais recente.



def contar_pessoas_por_ano():
    contagem_por_ano = {}
    for _ in range(1000):
        ano_nascimento = int(input())
        contagem_por_ano[ano_nascimento] = contagem_por_ano.get(ano_nascimento, 0) + 1
    return contagem_por_ano
    
    

def main():
    contagem_por_ano = contar_pessoas_por_ano()
    for ano, contagem in sorted(contagem_por_ano.items()):
            print(f"{ano}: {contagem}")



if __name__ =='__main__':
	main()