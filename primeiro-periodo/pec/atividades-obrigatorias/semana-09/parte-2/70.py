'''
Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a) "Telefonou para a vítima ?"

b) "Esteve no local do crime ?"

c) "Mora perto da vítima ?"

d) "Devia para a vítima ?"

e) "Já trabalhou com a vítima ?"

Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

def verificar_crime(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5):
    contador = 0
    if pergunta1 == "S":
        contador += 1
    if pergunta2 == "S":
        contador += 1
    if pergunta3 == "S":
        contador += 1
    if pergunta4 == "S":
        contador += 1
    if pergunta5 == "S":
        contador += 1
      
    if contador == 2:
        return f"Suspeito"
    elif contador == 3 or contador == 4:
        return f"Cúmplice"
    elif contador == 5:
        return f"Assassino"
    else:
        return f"Inocente"



def main():
    print("Considere “S” para sim ou “N” para não para as peguntas a seguir: ")
    pergunta1 = str(input("Telefonou para a vítima ?").strip().upper())
    pergunta2 = str(input("Esteve no local do crime ?").strip().upper())
    pergunta3 = str(input("Mora perto da vítima ?").strip().upper())
    pergunta4 = str(input("Devia para a vítima ?").strip().upper())
    pergunta5 = str(input("Já trabalhou com a vítima ?").strip().upper())
    resultado = verificar_crime(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)
    print(f"Foi verificado que o entrevistado é: {resultado}")



if __name__ == '__main__':
    main()