"""

18) Crie uma função `menor_maior_diferenca(lista)` que receba uma lista de números e retorne a
diferença entre o maior e o menor número da lista sem usar as funções `max` e `min`.

"""

def menor_maior_diferenca(lista):
    menor = lista[0]
    maior = lista[0]
    for num in lista:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    return maior - menor

def main():
    lista = []
    while True:
        try:
            num = input("Digite um número para a lista ou 'sair' para finalizar: ")
            if num.lower() == "sair":
                break
            lista.append(int(num))
            
        except ValueError:
            print("Entrada inválida! Digite um número.")
    if len(lista) > 0:
        print(f"A diferença entre o maior e o menor item na lista é: {menor_maior_diferenca(lista)}")
    else:
        print("A lista não foi criada!")

if __name__ == "__main__":
    main()