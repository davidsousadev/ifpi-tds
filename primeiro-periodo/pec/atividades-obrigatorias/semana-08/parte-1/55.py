'''
05. O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está
em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e
calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

IMC Classificação
< 18,5 Abaixo do peso
< 25 Peso normal
< 30 Sobrepeso
< 35 Obeso leve
< 40 Obeso moderado
>=40 Obeso mórbido
'''



def calculo(peso, altura):
    imc = peso/altura**2
    if(imc<=18.5):
        msg = ("Abaixo do peso")
        return imc, msg
    elif(imc>=18.5 and imc<=25):
        msg = 'Peso normal'
        return imc, msg 
    elif(imc>=25 and imc<=30):
        msg = 'Sobrepeso'
        return imc, msg 
    elif(imc>=30 and imc<=35):
        msg = 'Obeso leve'
        return imc, msg 
    elif(imc>=35 and imc<=40):
        msg = 'Obeso moderado'
        return imc, msg 
    elif(imc>=40):
        msg = 'Obeso mórbido'
        return imc, msg 



def main():
    peso = float(input("Qual é o seu peso: ").strip())
    altura = float(input("Quael é a sua altura: ").strip())
    imc, msg = calculo(peso, altura)
    print(f'Esse é o seu imc: ''%.2f'%imc)
    print(f'Essa é a sua situação: {msg}')



if __name__ == '__main__':
    main()
