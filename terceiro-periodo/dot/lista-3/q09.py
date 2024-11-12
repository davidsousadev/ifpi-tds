"""

9) Dada uma lista de palavras, escreva um programa que retorne uma nova lista contendo apenas
as palavras que começam com uma vogal. Exemplo: se `palavras = ["gato", "elefante", "urso",
"abelha", "cobra"]`, o programa deve retornar `["elefante", "urso", "abelha"]`.

"""


def filtrar_vogais(palavras):
    
    vogais = 'aeiouAEIOU'
    resultado = []
    for palavra in palavras:
        if palavra[0] in vogais:
            resultado.append(palavra)
            
    return resultado

def main():
    palavras = []
    while True:
        try:
            num = str(input("Digite uma palavra ou 'sair' para finalizar: ").strip())
            if num == "sair":
                break
            
            palavras.append(num)
            
        except ValueError:
            print("Entrada inválida! Digite uma palavra valida.")
             
    print(filtrar_vogais(palavras))

if __name__ == "__main__":
    main()