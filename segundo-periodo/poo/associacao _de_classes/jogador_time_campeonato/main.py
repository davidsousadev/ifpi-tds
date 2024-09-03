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
from random import randrange

class Campeonato: 
    def __init__(self, nome_campeonato, numero_de_times):
        self.__nome = nome_campeonato
        self.__numero_de_times = numero_de_times
        self.__times = {}
        self.__partidas = []
    
    def adicionarTimes(self, times):
        if len(times) > self.__numero_de_times:
            raise ValueError("Número de times excede o limite permitido.")
        for time in times:
            self.__times[time.nome_time] = 0

    def partida(self, time1, gols1, time2, gols2):
        if time1.nome_time not in self.__times or time2.nome_time not in self.__times:
            raise ValueError("Um ou ambos os times não estão no campeonato.")
        self.__partidas.append((time1.nome_time, time2.nome_time, gols1, gols2))
        if gols1 > gols2:
            self.__times[time1.nome_time] += 3
        elif gols1 < gols2:
            self.__times[time2.nome_time] += 3
        else:
            self.__times[time1.nome_time] += 1
            self.__times[time2.nome_time] += 1

    def mostrar_classificacao(self):
        print(f"Campeonato {self.__nome} com: {self.__numero_de_times} times\n")
        sorted_times = sorted(self.__times.items(), key=lambda item: item[1], reverse=True)
        print(f"{'Posição':<10}{'Time':<20}{'Pontos':<10}")
        print('-' * 40)
        for posicao, (time, pontos) in enumerate(sorted_times, start=1):
            print(f"{posicao:<10}{time:<20}{pontos:<10}")
        campeao = sorted_times[0][0]
        pontos = sorted_times[0][1]
        print(f"\nCampeão: {campeao} com {pontos} pontos.")
        

class Jogador:
    def __init__(self, nome, data_nasc, posicao):
        self.__nome_jogador = nome
        self.__data_nasc = data_nasc
        self.__posicao = posicao
        self.__time = None 

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
    def __init__(self, nome, estado):
        self.__nome_time = nome
        self.__estado = estado
        self.__jogadores = []

    @property
    def nome_time(self):
        return self.__nome_time

    def adiciona_jogador(self, jogador):
        if jogador not in self.__jogadores and jogador.idade() >= 18 and jogador.time is None: 
            self.__jogadores.append(jogador)
            jogador.novotime(self.__nome_time)
      
    def exclui_jogador(self, jogador):
        if jogador.time is not None and jogador.idade() >= 18:
            self.__jogadores.remove(jogador)
            jogador.novotime(None)
    
    def transferir_jogador(self, jogador, time):
        if jogador.time is not None and jogador.idade() >= 18:
            self.exclui_jogador(jogador)
            jogador.novotime(time.nome_time)
            time.adiciona_jogador(jogador)

    def mostrar_jogadores(self):
        print(f"Jogadores do time {self.__nome_time}: ")
        for jogador in self.__jogadores:
            print(f"{jogador.nome_jogador}")

def main():
    jogador1 = Jogador("David", '26/03/1996', "Zagueiro")
    jogador2 = Jogador("Pedro", '10/06/2006', "Volante")
    jogador3 = Jogador("Lucas", '15/08/1994', "Atacante")
    jogador4 = Jogador("Clayton", '22/12/1997', "Meia")
    jogador5 = Jogador("Ananias", '30/01/1995', "Goleiro")

    time1 = Time("São Paulo", "SP")
    time2 = Time("Atlético", "MG")
    time3 = Time("Flamengo", "RJ")
    time4 = Time("Grêmio", "RS")
    time5 = Time("Botafogo", "RJ")

    time1.adiciona_jogador(jogador1)
    time2.adiciona_jogador(jogador2)
    time3.adiciona_jogador(jogador3)
    time4.adiciona_jogador(jogador4)
    time5.adiciona_jogador(jogador5)  

    time1.exclui_jogador(jogador1)
    time1.transferir_jogador(jogador1, time2)
    time2.adiciona_jogador(jogador1)

    brasileiraobetano = Campeonato("Brasileirão Betano", 5)
    brasileiraobetano.adicionarTimes([time1, time2, time3, time4, time5])

    brasileiraobetano.partida(time1, randrange(0, 10), time2, randrange(0, 10))
    brasileiraobetano.partida(time1, randrange(0, 10), time3, randrange(0, 10))
    brasileiraobetano.partida(time1, randrange(0, 10), time4, randrange(0, 10))
    brasileiraobetano.partida(time1, randrange(0, 10), time5, randrange(0, 10))
    brasileiraobetano.partida(time2, randrange(0, 10), time3, randrange(0, 10))
    brasileiraobetano.partida(time2, randrange(0, 10), time4, randrange(0, 10))
    brasileiraobetano.partida(time2, randrange(0, 10), time5, randrange(0, 10))
    brasileiraobetano.partida(time3, randrange(0, 10), time4, randrange(0, 10))
    brasileiraobetano.partida(time3, randrange(0, 10), time5, randrange(0, 10))
    brasileiraobetano.partida(time4, randrange(0, 10), time5, randrange(0, 10))

    brasileiraobetano.partida(time2, randrange(0, 10), time1, randrange(0, 10))
    brasileiraobetano.partida(time3, randrange(0, 10), time1, randrange(0, 10))
    brasileiraobetano.partida(time4, randrange(0, 10), time1, randrange(0, 10))
    brasileiraobetano.partida(time5, randrange(0, 10), time1, randrange(0, 10))
    brasileiraobetano.partida(time3, randrange(0, 10), time2, randrange(0, 10))
    brasileiraobetano.partida(time4, randrange(0, 10), time2, randrange(0, 10))
    brasileiraobetano.partida(time5, randrange(0, 10), time2, randrange(0, 10))
    brasileiraobetano.partida(time4, randrange(0, 10), time3, randrange(0, 10))
    brasileiraobetano.partida(time5, randrange(0, 10), time3, randrange(0, 10))
    brasileiraobetano.partida(time5, randrange(0, 10), time4, randrange(0, 10))

    brasileiraobetano.mostrar_classificacao()

if __name__ == "__main__":
    main()
