'''
Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.
'''
def imprime_dez_em_dez():
    frase = ""
    for i in range(1,991):
        if(i%10==0):
            frase = f"{frase}"+f"{i}"+f", "
    frase = f"{frase}"+f"1000"+f"."
    return frase

def main():
    print(imprime_dez_em_dez())



if __name__ == '__main__':
    main()