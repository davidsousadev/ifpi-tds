"""

4) Crie uma lista `idades` com as idades de 10 pessoas. Escreva um código que divida essa lista 
em duas listas: uma com idades menores que 18 anos e outra com idades maiores ou iguais a 
18 anos.

"""
max_itens = 5
def main():
  idades = []
  maiores = 0 
  menores = 0
  for x in range(0,max_itens):
    while True:
      try:
        idade = int(input(f"Digite a idade da pessoa - {x + 1}: "))
        idades.append(idade)
        if idade>=18:
          maiores += 1
        else:
          menores += 1
        break
      except ValueError:
        print("Entrada inválida! Digite uma idade valida.")


  print(f"Maiores de idade: {maiores}")
  print(f"Menores de idade: {menores}")
  
if __name__ == "__main__":
    main()