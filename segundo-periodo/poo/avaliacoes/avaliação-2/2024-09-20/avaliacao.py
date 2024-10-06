"""
Alunos: David Sousa da Silva
Raissa Lorrana Lopes Da Rocha
"""

from abc import abstractmethod

class Veiculo():
    def __init__(self, modelo, nome, marca, ano, quilometros_rodados):
        self.modelo = modelo
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.quilometros_rodados = quilometros_rodados
    
    @abstractmethod
    def consumo_de_combustivel(self):
        raise NotImplementedError("Consumo de combustivel não implementado! ")
    
    def __str__(self):
        return f"Modelo: {self.modelo} - Nome: {self.nome} - Marca: {self.marca} - Ano: {self.ano}"

class Carro(Veiculo):
    def __init__(self, modelo, nome, marca, ano, quilometros_rodados):
        super().__init__(modelo, nome, marca, ano, quilometros_rodados)
        
    def consumo_de_combustivel(self):
        return  5.99 / 12
    
    def __str__(self) -> str:
        return super().__str__()
    
class Caminhao(Veiculo):
    def __init__(self, modelo, nome, marca, ano, quilometros_rodados):
        super().__init__(modelo, nome, marca, ano, quilometros_rodados)
        
    def consumo_de_combustivel(self):
        return 5.99 / 5
    
    def __str__(self) -> str:
        return super().__str__()

class Moto(Veiculo):
    def __init__(self, modelo, nome, marca, ano, quilometros_rodados):
        super().__init__(modelo, nome, marca, ano, quilometros_rodados)
        
    
    def consumo_de_combustivel(self):
        return  5.99 / 20
    
    def __str__(self) -> str:
        return super().__str__()

class Frota():
    def __init__(self):
        self.__veiculos = []      
           
    def adicionar_veiculo_a_frota(self, veiculo):
        return self.__veiculos.append(veiculo)
    
    def calcular_consumo_dos_veiculos(self):
        consumo = 0
        for veiculo in self.__veiculos:
            consumo += veiculo.consumo_de_combustivel()
        return consumo
    
    def limpar_frota(self):
        self.__veiculos = {}
        
    def remover_veiculo(self, index):
        for id, item in enumerate(self.__veiculos):
            if id <= len(self.__veiculos):
                if index-1==id:
                    self.__veiculos.pop(id)
                    return f"Veiculo excluido com sucesso!\n"
            else:
                return f"Veiculo não localizado!\n"
        
    def __str__(self):
        veiculos = ""
        total_quilometros = 0
        consumo_total = 0
        for veiculo in self.__veiculos:
            veiculos += f"Modelo: {veiculo.modelo} - Consumo: {(veiculo.quilometros_rodados * veiculo.consumo_de_combustivel()):.2f}\n"
            total_quilometros += veiculo.quilometros_rodados
            consumo_total += (veiculo.quilometros_rodados * veiculo.consumo_de_combustivel())   
        return f"{veiculos}Total de quilometros: {total_quilometros:.2f}\nConsumo Total: {consumo_total:.2f}\n"        
def main():
    # modelo, nome, marca, ano, quilometros_rodados
    carro01 = Carro("Siena","000", "Fiat", 2015, 12345)
    caminhao01 = Caminhao("IX5","111", "IVECO", 2019, 14723)
    moto01 = Moto("Titan", "160", "Honda", 2024, 12345)
    moto02 = Moto("Fan", "160", "Honda", 2024, 15623)
    
    frota01 = Frota()
    frota01.adicionar_veiculo_a_frota(carro01) 
    frota01.adicionar_veiculo_a_frota(caminhao01)
    frota01.adicionar_veiculo_a_frota(moto01)
    frota01.adicionar_veiculo_a_frota(moto02)
    
    
    print(frota01)
    print(frota01.remover_veiculo(3))
    print(frota01)
    frota01.limpar_frota()
    print(frota01)
    
if __name__ =="__main__":
    main()