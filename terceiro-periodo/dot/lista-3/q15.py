"""

15) Crie uma função que receba uma lista de números e retorne uma lista de tuplas, onde cada
tupla contenha um número e sua frequência na lista. Ordene a lista de tuplas por frequência em
ordem decrescente.
**Exemplo:** `lista = [4, 4, 3, 2, 4, 3]` -> `[(4, 3), (3, 2), (2, 1)]`

"""

def frequenciaNumeros(lista):
    frequencia = []
    
    while lista:
        num = lista[0]
        count = 0
        x = 0  
        while x < len(lista):
            if lista[x] == num:
                count += 1
                lista.pop(x)
            else:
                x += 1
        inserido = False
        for y in range(len(frequencia)):
            if count > frequencia[y][1]: 
                frequencia.insert(y, (num, count))
                inserido = True
                break
        if not inserido:
            frequencia.append((num, count))

    return frequencia

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
    # print(lista)         
    print(frequenciaNumeros(lista))

if __name__ == "__main__":
    main()
