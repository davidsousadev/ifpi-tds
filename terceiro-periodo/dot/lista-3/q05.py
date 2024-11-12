"""

5) Dada uma lista de números inteiros `numeros = [3, 6, 9, 12, 15, 18]`, escreva um código para 
encontrar e remover o maior número da lista sem usar a função `max`.

"""
def main():
  maior = 0
  numeros = [3, 6, 9, 12, 15, 18]
  id = None
  for num in numeros:
    # print(num)
    if num >= maior:
      id = numeros.index(num)
      maior = num

  numeros.pop(id)
  print(numeros)

if __name__ == "__main__":
    main()