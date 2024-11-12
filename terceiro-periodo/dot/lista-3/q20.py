"""

20) Escreva uma função que receba uma lista de números e retorne uma nova lista onde cada
elemento é o produto de todos os outros números na lista, exceto ele mesmo (sem usar divisão).
**Exemplo:** Para `[1, 2, 3, 4]`, a função deve retornar `[24, 12, 8, 6]`.

"""

def produtoExcetoEleMesmo(lista):
    
    resultado = []
    for x in range(len(lista)):
        produto = 1
        for y in range(len(lista)):
            if x != y:
                produto *= lista[y]
        resultado.append(produto)
        
    return resultado

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
            
    print(lista)
    print(produtoExcetoEleMesmo(lista))

if __name__ == "__main__":
    main()