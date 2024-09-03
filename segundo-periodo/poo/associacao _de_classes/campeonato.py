"""
Com base nas classes definidas no exercício anterior, crie uma nova classe chamada: Campeonato com os seguintes atribuitos:
Numero_times (responsável por limitar a quantidade de times participantes do campeonato), times (representando uma lista de instancias de times participantes), partidas (representando uma partida entre dois times e o resultado da partida). Sugestão: pode criar uma tupla com 4 informações: time_casa, time_visitante, placar_time_casa, placar_time_visitante.

Para cada partida registrada, contabilizar:
3 pontos para o time vencedor
0 pontos para o time perdedor
1 ponto para cada time em caso de empate.

Sugestão: criar um dicionário para o atributo times com chave=Time e valor=pontuação

Criar um método: mostrar_classificação(...) para imprimir a pontuação dos times em ordem decrescente.

A classe Campeonato vai ser a classe agregadora de Time. (1:N)

"""

from datetime import datetime

class Campeonato: 
    def __init__(self, numero_de_times):
        self.__numero_de_times = numero_de_times
        self.__times = {}
        self.__partidas = ()
    
    def adicionarTimes(self, time):
       self.__times = time

    def tabela(self):
       pass

    def partida(self, time1, gols1, time2, gols2):
       if gols1>gols2:
          self.__times[time1] += 3
       if gols1==gols2:
          self.__times[time1] += 1
          self.__times[time2] += 1
       if gols1<gols2:
          self.__times[time2] += 3
    



class Jogador:
  def __init__(self,nome,data_nasc,posição):
    self.__nome_jogador = nome
    self.__data_nasc = data_nasc
    self.__posição = posição
    self.__time = None #time vinculado ao jogador

  @property
  def nome_jogador(self):
    return self.__nome_jogador

  @property
  def posicao(self):
    return self.__posicao

  @property
  def time(self):
    return self.__time
  
  
  def novotime(self, novotime):
    self.__time = novotime 

  def idade(self):
        data_nascimento = datetime.strptime(self.__data_nasc, '%d/%m/%Y')
        hoje = datetime.today()
        idade = hoje.year - data_nascimento.year
        if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade

class Time:
  def __init__(self,nome,estado):
    self.__nome_time = nome
    self.__estado = estado
    self.__jogadores = []

  @property
  def nome_time(self):
    return self.__nome_time



  def adiciona_jogador(self, jogador):
      if jogador is not self.__jogadores and jogador.idade() >= 18 and jogador.time == None: 
        self.__jogadores.append(jogador)
        print(f"Jogador: {jogador.nome_jogador}, Time: {self.__nome_time}")
        jogador.novotime(self.__nome_time)
      

  def exclui_jogador(self, jogador):
   if jogador.time !=None and jogador.idade() >= 18:
    self.__jogadores.remove(jogador)
    jogador.novotime(None)
    

  def transferir_jogador(self,jogador, time):
   if jogador.time !=None and jogador.idade() >= 18:
     self.exclui_jogador(jogador)
     jogador.time = time
     self.adiciona_jogador(jogador)
   


  def mostrar_jogadores(self):
    print(f"Jogadores do time {self.__nome_time}: ")
    for jogador in self.__jogadores:
      print(f"{jogador.nome_jogador}")


def main():
    jogador1 = Jogador("David", '26/03/1996', "Zagueiro")
    jogador2 = Jogador("Pedro", '26/03/2006', "Zagueiro")
    time1 = Time("Star Wars", "PI")
    time2 = Time("Altos", "PI")
    time3 = Time("Flamengo", "PI")
    # time4 = Time("Jose de Freitas", "PI")

    # Adicionar jogador 
    time1.adiciona_jogador(jogador1)
    time2.adiciona_jogador(jogador2)
    
    brasileiraobetano = Campeonato(3)
    brasileiraobetano.adicionarTimes({time1.nome_time : 0, time2.nome_time : 0, time3.nome_time: 0})
    
    brasileiraobetano.partida(time1.nome_time, 1, time2.nome_time, 4)
    brasileiraobetano.partida(time3.nome_time, 7, time1.nome_time, 1)
    brasileiraobetano.tabela()

    # time1.exclui_jogador(jogador1)
    # time1.transferir_jogador(jogador1, time2)
    # time1.mostrar_jogadores()
    #time2.adiciona_jogador(jogador1)
    #  time2.mostrar_jogadores()

if __name__=="__main__":
    main()