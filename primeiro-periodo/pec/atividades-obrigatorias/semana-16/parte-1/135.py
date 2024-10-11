# Escreva um programa que lê matrícula, nome e duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é a matrícula do aluno. A entrada de dados deve terminar quando for lida uma string vazia como matrícula. Escreva uma função que retorna a média do aluno, dado sua matrícula, o programa finaliza com a leitura de uma matrícula vazia,



def calcular_media(matricula, dicionario_alunos):
    if matricula in dicionario_alunos:
        notas = dicionario_alunos[matricula]
        media = sum(notas['notas']) / len(notas['notas'])
        return media
    else:
        return None



def adicionar_notas():
    notas_alunos = {}
    while True:
        matricula = str(input().strip())
        if matricula == "":
            break
        nome = str(input().strip())
        nota1 = float(input())
        nota2 = float(input())
        notas_alunos[matricula] = {"nome": nome, "notas": [nota1, nota2]}
    return notas_alunos
    
    
    
def main():
    notas_alunos = adicionar_notas()
    
    while True:
        matricula_consulta = str(input().strip())
        if matricula_consulta == "":
            break
        media = calcular_media(matricula_consulta, notas_alunos)
        if media is not None:
            nome_aluno = notas_alunos[matricula_consulta]["nome"]
            print(f"{nome_aluno}: {media:.1f}")
            
            

if __name__ =='__main__':
	main()