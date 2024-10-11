class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado_civil, estado="vivo", conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = self.valida_sexo(sexo)
        self.__estado_civil = self.valida_estado_civil(estado_civil)
        self.__estado = estado
        self.__conjuge = conjuge
    
    def valida_sexo(self, sexo):
        sexos = ['M', 'F']
        if sexo in sexos:
            return sexo
        else:
            raise ValueError(f"Sexo inválido: {sexo}")
                
    def valida_estado_civil(self, estado_civil):
        estados_civis = ['solteiro', 'casado', 'viúvo']
        if estado_civil in estados_civis:
            return estado_civil
        else:
            raise ValueError(f"Estado civil inválido: {estado_civil}")
                                       
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def estado_civil(self):
        return self.__estado_civil
    
    @estado_civil.setter
    def estado_civil(self, novo_estado_civil):
        self.__estado_civil = self.valida_estado_civil(novo_estado_civil)
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def conjuge(self):
        return self.__conjuge
    
    @conjuge.setter
    def conjuge(self, novo_conjuge):
        self.__conjuge = novo_conjuge
    
    def falecer(self):
        self.__estado = "morto"
    
    def casar(self, conjuge):
        if self.__estado_civil == "solteiro" and conjuge.estado_civil == "solteiro":
            self.estado_civil = "casado"
            self.conjuge = conjuge
            conjuge.estado_civil = "casado"
            conjuge.conjuge = self
        else:
            raise ValueError("Uma das pessoas já está casada")

def main():
    try:
        pessoa1 = Pessoa("João", 30, 70, 175, "M", "solteiro")
        pessoa2 = Pessoa("Maria", 28, 60, 165, "F", "solteiro")
        pessoa1.casar(pessoa2)
        print(f"{pessoa1.nome} e {pessoa2.nome} estão casados.")
    except ValueError as e:
        print(e)
    
if __name__ == '__main__':
    main()
