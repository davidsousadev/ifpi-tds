"""

IFPI
CURSO: TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
DISCIPLINA: PROGRAMAÇÃO ORIENTADA À OBJETOS
PROF.: ROGÉRIO BATISTA

EXERCÍCIO - ASSOCIAÇÃO DE CLASSES 1:1

"""

import random

class Bateria:
    seg = 0

    def __init__(self, capacidade):
        Bateria.seg += 1 
        self.__codigo = Bateria.seg
        self.__capacidade = capacidade
        self.__percentual_carga = random.randint(0, 100)  
        
    @property    
    def codigo(self):
        return self.__codigo
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property  
    def carga(self):
        return self.__percentual_carga
    
    # Método solicitado - Carregar(self,valor)
    def carregar(self, valor):
        if self.__percentual_carga + valor > 100:
            self.__percentual_carga = 100
        else:
            self.__percentual_carga += valor
        print(f"Bateria carregada para {self.__percentual_carga}%.")
        
    # Método solicitado - Descarregar(self,valor)
    def descarregar(self, valor):
        if self.__percentual_carga - valor < 0:
            self.__percentual_carga = 0
        else:
            self.__percentual_carga -= valor
        print(f"Bateria descarregada para {self.__percentual_carga}%.")

class Celular:
    def __init__(self, mei):
        self.__mei = mei
        capacidade = int(input(f"Capacidade da bateria do celular mei - {mei}: "))  
        self.__bateria = Bateria(capacidade) # Criando a instância Bateria
        self.__wifi = False
        self.__estado = False
    
    # Método solicitado - LigarDesligar(self)     
    def ligardesligar(self):
        if not self.__estado:
            if self.__bateria and self.__bateria.carga > 0:
                self.__estado = True
                print(f"Celular ligado com {self.__bateria.carga}% de carga.")
            else:
                print("Não foi possível ligar! Sem bateria ou bateria descarregada.")
        else:
            self.__estado = False
            print("Celular desligado.")
    
    # Método solicitado - colocarBateria(self, bateria)
    def colocar_bateria(self, bateria):
        if self.__bateria is None:
            self.__bateria = bateria
            print(f"Bateria de código: {bateria.codigo} colocada no celular.")
        else:
            print("O celular já possui uma bateria.")

    def retirar_bateria(self):
        if self.__bateria is not None:
            print(f"Bateria de código: {self.__bateria.codigo} retirada do celular.")
            self.__bateria = None
        else:
            print("O celular está sem bateria.")
            
    # Método solicitado - LigarDeslgarWifi(self)
    def ligar_desligar_wifi(self):
        self.__wifi = not self.__wifi
        estado = 'ligado' if self.__wifi else 'desligado'
        print(f"WiFi: {estado}")

    # Método solicitado - assistirVideo(self,tempo)
    def assistir_video(self, tempo):
        if self.__wifi and self.__bateria and self.__estado:
            consumo = tempo * 5
            if self.__bateria.carga >= consumo:
                self.__bateria.descarregar(consumo)
                print(f"Você assistiu {tempo} minutos de vídeo.")
            else:
                print("Bateria insuficiente para assistir o vídeo.")
                self.__bateria.descarregar(self.__bateria.carga)
        else:
            print("Para assistir vídeo, o WiFi deve estar ligado, o celular deve estar ligado e a bateria deve estar carregada.")

    # Método solicitado - Carregar (self, valor) -
    def carregar(self, valor):
        if self.__bateria:
            self.__bateria.carregar(valor)
        else:
            print("Celular sem bateria.")
    # Método solicitado - Descarregar(self, valor)
    def descarregar(self, valor):
        if self.__bateria:
            self.__bateria.descarregar(valor)
        else:
            print("Celular sem bateria.")

    def __str__(self):
        wifi_estado = 'ligado' if self.__wifi else 'desligado'
        estado_celular = 'ligado' if self.__estado else 'desligado'
        bateria_info = f"{self.__bateria.capacidade} mAh, Carga: {self.__bateria.carga}%" if self.__bateria else "Sem bateria"
        
        return (f"Mei: {self.__mei}\nBateria: {bateria_info}\nWiFi: {wifi_estado}\nCelular: {estado_celular}\n")
