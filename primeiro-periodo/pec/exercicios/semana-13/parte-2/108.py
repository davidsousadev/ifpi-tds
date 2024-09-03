#Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).



def inserirItens(notas, indices_notas_altas):
    for i in range(50):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
        if nota >= 6:
            indices_notas_altas.append(nota)
    return notas, indices_notas_altas

def main():
    notas = []
    indices_notas_altas = []
    notas, indices_notas_altas = inserirItens(notas, indices_notas_altas)
    print(f"Notas maior ou igual a 6 (seis): {indices_notas_altas}")

if __name__ == "__main__":
    main()
