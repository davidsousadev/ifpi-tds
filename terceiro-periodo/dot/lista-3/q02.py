"""

2) Dada uma lista `nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]`, escreva 
um código para contar quantos nomes têm mais de cinco letras.

"""

def main():
  
  nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]

  qtd = 0

  for nome in nomes: 
    if len(nome) > 5:
      qtd += 1


  print(f"Quantidade de nomes com mais de cinco letras: {qtd}")

if __name__ == "__main__":
    main()