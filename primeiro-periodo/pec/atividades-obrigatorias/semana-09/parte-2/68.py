'''
Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.

OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.


'''
def verificaData(data):
    dia = data // 1000000
    mes = data // 10000 - (dia * 100)
    ano = data -((data // 10000) *10000)
    if  ano > 0:
        if 1 <= mes <= 12:
            if dia <= 31 and dia > 0 and mes ==1: 
                return True
            if 1 <= dia <= 29 and mes == 2 and ano %4 == 0 :
                return True
            if 1 <= dia <= 28 and mes == 2 and ano %4 != 0:
                return True
            elif 1 <= dia <= 31 and mes == 3:
                return True
            elif 1 <= dia <= 30 and mes == 4: 
                return True
            elif 1 <= dia <= 31 and mes == 5: 
                return True
            elif 1 <= dia <= 30 and mes == 6:
                return True
            elif 1 <= dia <= 31 and mes == 7: 
                return True
            elif 1 <= dia <= 31 and mes == 8: 
                return True
            elif 1 <= dia <= 30 and mes == 9: 
                return True
            elif 1 <= dia <= 31 and mes == 10: 
                return True
            elif 1 <= dia <= 30  and mes == 11: 
                return True
            elif 1 <= dia <= 31 and  mes == 12: 
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def main():
    print("Esse programa vai verificar se uma data é valida.")
    data = int(input("Digite uma data exemplo 26031996: "))
    resultado=verificaData(data)
    if resultado==True:
        print(f"{resultado} = Essa data é valida!")
    else:
        print(f"{resultado} = Essa data é invalida!")



if __name__ == '__main__':
    main()