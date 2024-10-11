import time
class radio:
    modelo=None
    marca=None
    volume_atual=0
    estacao_atual=0
    porcentagem_bateria_atual=0
    estado=None
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca
    def ligar(self):
        if self.porcentagem_bateria_atual>0:
            self.estado = True
            print("Ligado")
            print("Buscando estação")
            print(self.buscar_estacao())
            while True:
                if self.porcentagem_bateria_atual>0:
                    self.descarregar_bateria()
                else:
                    print(f"Bateria em {self.porcentagem_bateria_atual} %")
                    self.desligar()
                    break
    def buscar_estacao(self):
        if self.porcentagem_bateria_atual>0 and self.estado==True:
                return f"99.9 MHz"  
    def desligar(self):
        self.estado = False
        print("Desligado")
    def descarregar_bateria(self):
        self.porcentagem_bateria_atual -= 1
        time.sleep(0.1)
        return self.porcentagem_bateria_atual
    def carregar_bateria(self):
        print("Bateria Carregando!!!")
        for i in range(100):
            if self.porcentagem_bateria_atual<100:
                self.porcentagem_bateria_atual = 1+self.porcentagem_bateria_atual
        time.sleep(0.1)
        print("Carga completa")


radio1 = radio("Novo","Nova")
radio1.porcentagem_bateria_atual = 50
radio1.ligar()


radio2 = radio("Radio","Inova")
radio2.porcentagem_bateria_atual = 78
radio2.ligar()
radio2.carregar_bateria()


radio3 = radio("Radio","Inova")
radio3.porcentagem_bateria_atual = 33
radio3.ligar()



