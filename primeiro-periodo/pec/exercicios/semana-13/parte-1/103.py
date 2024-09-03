# Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.



def listaReverso(n):
    l = []
    for c in range(n):
        x = float(input("Digite um valor para inserir a lista: "))
        l.insert(0, x)
    return f"Reverso da lista: {l}"
    
    
    
def listaNotas(n):
    l = []
    soma = 0
    if (n == 0):
        print(f"{l}\nSEM NOTAS")
    else:
        for x in range(n):
            nota = float(input("Digite as notas: "))
            l.append(nota)
            soma += nota
        media = soma / n
        return f"Lista com as notas: {l} Media das notas: \n{media:.1f}"
        
        
        
def vogaisEConsoantes(n):
    lista = []
    vogais = "aeiouAEIOU"
    contador = 0
    for x in range(n):
        letra = str(input("Digite caracteres: ")[0].strip())
        lista.append(letra)
        if letra in vogais:
            contador += 1
            lista.remove(letra)
    return f"Quantidade de vogais inseridas: {contador} Lista com as consoantes: \n{lista}"
    
    
    
def main():
    n = int(input("Digite a quantidade de itens na lista: "))
    print(f"{listaReverso(n)}")
    print(f"{listaNotas(n)}")
    print(f"{vogaisEConsoantes(n)}")
if __name__ == '__main__':
    main()