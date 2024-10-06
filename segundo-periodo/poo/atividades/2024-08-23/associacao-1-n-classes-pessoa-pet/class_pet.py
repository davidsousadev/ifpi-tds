"""
Carlos Samuel Freitas Barbosa
David Sousa da Silva
Raissa Lorrana Lopes da Rocha

"""

class Pet:
  def __init__(self,tipo,nome,idade,peso,raca,cor,castrado=False,origem = None):
    self.__tipo = tipo
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__raca = raca
    self.__cor = cor
    self.__castrado = castrado
    self.__origem = origem


  @property
  def origem(self):
    return self.__origem    

  @property
  def nome(self):
    return self.__nome

  def __str__(self):
    return f'Tipo: {self.__tipo}\nNome: {self.__nome}\nIdade: {self.__idade}\nPeso: {self.__peso}\nRaça: {self.__raca}\nCor: {self.__cor}\nCastrado: {self.__castrado}\nOrigem: {self.__origem}\n'


class Pessoa:
  def __init__(self,cpf,nome,endereco):
    self.__cpf = cpf
    self.__nome = nome
    self.__endereco = endereco
    self.__meus_pets = []


  @property
  def cpf(self):
    return self.__cpf

  @property
  def nome(self):
    return self.__nome
  
  @property
  def enderco(self):
    return self.__endereco

  def cadastrar_pet(self,pet):
    self.__meus_pets.append(pet)
    print(f'O pet {pet.nome} foi cadastrado com sucesso!')

  def excluir_pet(self,nome):
    for pet in self.__meus_pets:
      if pet.nome == nome:
        self.__meus_pets.remove(pet)
        print(f'O pet {pet.nome} foi excluido com sucesso!')
        return True
    return False
  
  def mostrar_meus_pets(self):
    print(f"\nPets da {self.__nome}:")
    for pet in self.__meus_pets:
        print(f"{pet}")

# Criando pessoas e seus pets
pessoa1 = Pessoa("12345678901", "João Silva", "Rua A, 123")
pessoa2 = Pessoa("98765432109", "Maria Souza", "Rua B, 456")
pessoa3 = Pessoa("11122233344", "Pedro Santos", "Rua C, 789")


# Cadastrando pets para as pessoas
pet1 = Pet("cachorro", "Chocolate", 3, 26, "Labrador", "Marrom", True, "abrigo")
pet2 = Pet("gato", "Tintin", 1, 4, "Siamês", "Branco e Preto", True, "rua")

pet3 = Pet("cachorro", "Tokin", 2, 3, "Pastor Alemão", "Preto", True, "abrigo")

pet4 = Pet("gato", "Romeu", 4, 20, "Europeu", "Branco e laranja", True, "rua")



pessoa3.cadastrar_pet(pet4)
pessoa2.cadastrar_pet(pet3)
pessoa1.cadastrar_pet(pet1)
pessoa1.cadastrar_pet(pet2)

# Mostrando os pets da pessoa1 antes da exclusão
print("Pets da pessoa1 antes da exclusão:")
pessoa1.mostrar_meus_pets()

# Excluindo um pet
pessoa1.excluir_pet("Rex")

# mostrar meus pets

pessoa1.mostrar_meus_pets()
pessoa2.mostrar_meus_pets()
