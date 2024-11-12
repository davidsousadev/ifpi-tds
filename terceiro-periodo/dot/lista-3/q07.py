"""

7) Crie uma lista `temperaturas = [23.5, 18.6, 30.2, 15.9, 25.1, 29.8]` e escreva um código para
encontrar a média das temperaturas. Imprima a média ao final.

"""
def mediaTemperaturas(temperaturas):
    
    soma = 0
    for temperatura in temperaturas:
        soma += temperatura
    
    if temperaturas:
        media = soma / len(temperaturas) 
    else:
        media = 0
        
    return media

def main():
    temperaturas = []
    while True:
        try:
            temperatura = input("Digite uma temperatura ou 'sair' para finalizar: ")
            if temperatura == "sair":
                break
            temperaturas.append(float(temperatura))
        except ValueError:
             print("Entrada inválida! Digite uma temperatura valida.")
    
    
        
    print("Média das temperaturas:", mediaTemperaturas(temperaturas))

if __name__ == "__main__":
    main()