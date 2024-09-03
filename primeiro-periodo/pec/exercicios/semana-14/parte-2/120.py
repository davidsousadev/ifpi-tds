# Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.




def inserirItens():
  lista = []
  for i in range(10):
    num = int(input("Digite um numero: "))
    lista.append(num)
  return lista



def unirListas(lista1, lista2):
    uniao = []
    for numero in lista1:
        if numero not in uniao:
            uniao.append(numero)
    for numero in lista2:
        if numero not in uniao:
            uniao.append(numero)   
    return uniao


def main():
    lista1 = inserirItens()
    lista2 = inserirItens()
    uniao = unirListas(lista1, lista2)
    print(f"Essa e a uniao das listas: {uniao}")



if __name__ == '__main__':
    main()