'''Impementar uma associação de classes 1:N entre as classes: Time e Jogador, onde a classe agregadora é a classe Time.

Métodos: 

adicionar_jogador(...)
# adiciona um jogador sem vínculo com outro time

exclui_jogador(...)
# exclui jogador de um time 

transferir_jogador(...)

   # método que transfere um jogador de um time A (self) para um time B (time)
   # Jogador precisa ser maior de idade (>=18)
   #reutilizar os métodos: adiciona_jogador e exclui_jogador

Mostrar_jogador(...)

#mostra a lista com a informação dos jogadores do time


No main(), crie objetos para representar pelo menos 4 times. Adicione jogadores menores de idade e maiores de idade diretamente do método adicionar_jogador(...). Crie objetos que representem jogadores sem vínculo. Adicione estes jogadores aos times. Realize transações entre times (transferencias). Exclua jogadores tornado-os sem vinculo.
'''


from datetime import datetime

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
        print(f"Jogador: {jogador.time} Time: {self.__nome_time}")
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
  jogador2 = Jogador("Jose", '26/03/1996', "Zagueiro")
  time1 = Time("Star Wars", "PI")
  time2 = Time("Altos", "PI")
  time3 = Time("Flamengo", "PI")
  time4 = Time("Jose de Freitas", "PI")
  time1.adiciona_jogador(jogador1)
  time1.exclui_jogador(jogador1)
  time1.transferir_jogador(jogador1, time2)
  time1.mostrar_jogadores()
  time2.adiciona_jogador(jogador1)
  time2.mostrar_jogadores()

if __name__ == '__main__':
  main()
  