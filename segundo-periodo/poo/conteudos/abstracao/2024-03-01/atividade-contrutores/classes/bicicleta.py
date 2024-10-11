class bicicleta:
    peso=None
    altura=None
    veloc_atual=0
    veloc_max=None
    cor=None
    aro=0
    altura_cela=0
    altura_cela_max=None
    calibragem_pneus=0
    calibragem_pneus_max=None
    def __init__(self,peso,altura,cor,aro,altura_cela_max, calibragem_pneus_max):
        self.peso = peso
        self.altura = altura
        self.cor = cor
        self.aro = aro
        self.altura_cela_max = altura_cela_max
        self.calibragem_pneus_max = calibragem_pneus_max
    def peladar(self,velocidade):
        self.veloc_atual +=velocidade
    def frear(self):
        self.veloc_atual=0
    def regular_cela(self,regulagem):
        if self.altura_cela+regulagem<=self.altura_cela_max:
            self.altura_cela += regulagem
    def calibrar_peneus(self,calibragem):
        if self.calibragem_pneus+calibragem<=self.calibragem_pneus_max:
            self.calibragem_pneus += calibragem

monark = bicicleta("10","56","Azul metálico",27.5,95,60)
print(f" Velocidade Atual: {monark.veloc_atual}")
print(f" Altura da Cela: {monark.altura_cela}")
print(f" Calibragem dos Pneus: {monark.calibragem_pneus}")
monark.peladar(5)
monark.regular_cela(12)
monark.calibrar_peneus(8)
print(f" Velocidade Atual: {monark.veloc_atual}")
print(f" Altura da Cela: {monark.altura_cela}")
print(f" Calibragem dos Pneus: {monark.calibragem_pneus}")

houston = bicicleta("11","60","Preto fosco",29,90,50)
print(f" Velocidade Atual: {houston.veloc_atual}")
print(f" Altura da Cela: {houston.altura_cela}")
print(f" Calibragem dos Pneus: {houston.calibragem_pneus}")
houston.peladar(7)
houston.regular_cela(10)
houston.calibrar_peneus(15)
print(f" Velocidade Atual: {houston.veloc_atual}")
print(f" Altura da Cela: {houston.altura_cela}")
print(f" Calibragem dos Pneus: {houston.calibragem_pneus}")