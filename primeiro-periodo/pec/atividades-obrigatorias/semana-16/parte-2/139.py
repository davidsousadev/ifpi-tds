# Suponha que vamos jogar um dado e queremos saber quantas vezes cada face (de 1 a 6) caiu. Faça um programa que leia o resultado de cada jogada do dado e armazena em um dicionário. A face do dado é a chave para o dicionário e a leitura de um valor 0 (zero) na face encerra o jogo. Mostre quantas vezes o dado foi lançado e quantas vezes cada face saiu. A leitura do valor 0 (zero) para a face encerra o jogo e mostra o resultado.

def jogar_dados():
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    total_lancamentos = 0
    while True:   
        resultado = int(input())  
        if resultado == 0:
            break    
        total_lancamentos += 1  
        if 1 <= resultado <= 6:
            resultados[resultado] += 1
    return total_lancamentos, resultados    
            
            
def main():
    total_lancamentos, resultados = jogar_dados()
    print(f"{total_lancamentos} {resultados}")




if __name__ =='__main__':
	main()