estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

class RadioFM:
    def __init__(self,vol_max,estacoes):
        self.volume_min=0
        self.volume_max=vol_max
        self.freq_min=88
        self.freq_max=108
        self.estacoes=estacoes
        self.volume=None
        self.ligado=False
        self.estacao_atual=None
        self.frequencia_atual=None
        self.antena_habilitada=False
    
    def habilitar_antena(self):
        if self.antena_habilitada==False:
            self.antena_habilitada=True
        else:
            self.antena_habilitada=False

    def ligar_desligar(self, estado=False):
        if estado==False and self.antena_habilitada==True:
                self.ligado=True
                self.volume=self.volume_min
                frequencias = list(self.estacoes.items())
                self.frequencia_atual=frequencias[0][0]
                self.estacao_atual=self.estacoes[self.frequencia_atual]
        else:
            self.ligado=False
            self.frequencia_atual=None
            self.estacao_atual=None
            self.antena_habilitada=False


    def aumentar_diminuir_volume(self, volume=1):
        if self.ligado==True:
            if self.volume+volume<=self.volume_max and self.volume+volume>=self.volume_min:
                self.volume+=volume

    def mudar_frequencia(self,frequencia=0):
        if frequencia!=0 and self.ligado==True:
            try:
                if self.estacoes[frequencia]:
                    frequencias = list(self.estacoes.items())
                    if frequencias[-1][0]==frequencia:
                        self.frequencia_atual=frequencias[0][0]
                        self.estacao_atual=self.estacoes[self.frequencia_atual] 
                    else:    
                        self.estacao_atual=self.estacoes[frequencia]
                        self.frequencia_atual=frequencia
            except:
                self.estacao_atual="Estação inexistente."
                self.frequencia_atual=None
        
        
# Objeto Radio001
Radio001 = RadioFM(100,estacoes)
Radio001.habilitar_antena()
Radio001.ligar_desligar()
Radio001.mudar_frequencia(99.1)
Radio001.aumentar_diminuir_volume(99)
Radio001.aumentar_diminuir_volume(-99)

# Objeto Radio002
Radio002 = RadioFM(100,estacoes)
Radio002.habilitar_antena()
Radio002.ligar_desligar()
Radio002.mudar_frequencia(94.1)

# Objeto Radio003
Radio003 = RadioFM(100,estacoes)
Radio003.habilitar_antena()
Radio003.ligar_desligar(True)
Radio003.mudar_frequencia(99.9)

print(Radio001.frequencia_atual)
print(Radio001.estacao_atual)
print(Radio001.volume)

print(Radio002.frequencia_atual)
print(Radio002.estacao_atual)
print(Radio002.volume)

print(Radio003.frequencia_atual)
print(Radio003.estacao_atual)
print(Radio003.volume)