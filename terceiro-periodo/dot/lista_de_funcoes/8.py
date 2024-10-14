"""

8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'.  Se o 
caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um 
programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os 
números até o usuário responder 'N' à pergunta se ele deseja continuar ou não. 

"""
def le_caractere():
    while True:
        try:
            caractere = input("Digite 'S' para continuar ou 'N' para parar: ").upper()
            if caractere in ['S', 'N']:
                return caractere
        except ValueError:
            print("Caractere inválido. Digite novamente.")

while True:
    try:
        numero = float(input("Digite um número: "))
        print(f"O número ao cubo é: {numero ** 3}")
        if le_caractere() == 'N':
            break
    except ValueError:
        print("\nDigite um número inteiro valido!\n")

