"""

1) Crie uma lista com números inteiros de 1 a 10. Em seguida, use um loop para encontrar a soma 
de todos os números pares dessa lista.

"""
from random import randint

def somaPares(lista, soma):
  
  for _ in range(1,11):
    x = randint(0, 100)
    lista.append(x)
    if x%2==0:
      soma += x
      
  return lista, soma


def main():
  
  lista = []
  soma = 0
  lista, soma = somaPares(lista, soma)
  print(f"Lista: {lista}")
  print(f"Soma dos pares: {soma}")

if __name__ == "__main__":
    main()