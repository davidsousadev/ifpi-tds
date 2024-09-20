from datetime import datetime, timedelta

# 1. Criação da classe base com exemplo de encapsulamento e abstração.
class Pessoa:
    def __init__(self, nome, idade):
        # Atributos privados (encapsulamento)
        self.__nome = nome
        self.__idade = idade
    
    # Getter para o nome (acessando o atributo privado)
    @property
    def nome(self):
        return self.__nome

    # Setter para o nome (modificando o atributo privado)
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError("Nome deve ser uma string válida.")

    # Método público
    def aniversario(self):
        # Exemplo de método que altera o estado do objeto
        self.__idade += 1
        print(f"Parabéns {self.__nome}, você agora tem {self.__idade} anos!")

    # Método abstrato (que pode ser sobrescrito em subclasses)
    def falar(self):
        raise NotImplementedError("Este método deve ser sobrescrito.")

# 2. Herança: Criação de uma subclasse que herda de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        # Chamada ao construtor da superclasse (reuso)
        super().__init__(nome, idade)
        self.cargo = cargo
        self.data_contratacao = datetime.now()
    
    # Sobrescrita do método falar (polimorfismo)
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e trabalho como {self.cargo}.")
    
    # Método para calcular o tempo de empresa
    def tempo_de_empresa(self):
        # Diferença entre a data atual e a data de contratação
        tempo = datetime.now() - self.data_contratacao
        return tempo.days

# 3. Outra subclasse: Associação entre classes
class Projeto:
    def __init__(self, nome_projeto, prazo_dias):
        self.nome_projeto = nome_projeto
        self.prazo_entrega = datetime.now() + timedelta(days=prazo_dias)
        self.funcionarios_envolvidos = []  # Associação
    
    def adicionar_funcionario(self, funcionario):
        # Exemplo de associação: um projeto tem vários funcionários
        if isinstance(funcionario, Funcionario):
            self.funcionarios_envolvidos.append(funcionario)
        else:
            raise ValueError("Somente funcionários podem ser associados a um projeto.")

    # Método que exibe os detalhes do projeto
    def detalhes_projeto(self):
        print(f"Projeto: {self.nome_projeto}")
        print(f"Prazo de entrega: {self.prazo_entrega}")
        print(f"Funcionários envolvidos:")
        for funcionario in self.funcionarios_envolvidos:
            print(f"- {funcionario.nome} ({funcionario.cargo})")

# 4. Exemplo de herança e polimorfismo
class Gerente(Funcionario):
    def __init__(self, nome, idade):
        # O gerente é um funcionário com cargo específico
        super().__init__(nome, idade, cargo="Gerente")
    
    # Reescrita do método falar para gerente
    def falar(self):
        print(f"Olá, meu nome é {self.nome}, sou gerente e estou coordenando os projetos.")

    # Método específico para gerente
    def aprovar_projeto(self, projeto):
        if isinstance(projeto, Projeto):
            print(f"O projeto {projeto.nome_projeto} foi aprovado por {self.nome}.")
        else:
            print("Isso não é um projeto válido.")

# 5. Uso do código
def main():
    # Criando instâncias de Pessoa e Funcionario
    joao = Funcionario(nome="João", idade=30, cargo="Desenvolvedor")
    maria = Gerente(nome="Maria", idade=40)
    
    # Exemplo de chamada a métodos de instâncias
    joao.falar()  # Polimorfismo: o método falar tem comportamentos diferentes
    maria.falar()
    
    # João faz aniversário
    joao.aniversario()

    # Criando um projeto e associando funcionários
    projeto1 = Projeto(nome_projeto="Sistema Web", prazo_dias=60)
    projeto1.adicionar_funcionario(joao)
    projeto1.adicionar_funcionario(maria)

    # Exibindo os detalhes do projeto
    projeto1.detalhes_projeto()

    # Gerente aprovando o projeto
    maria.aprovar_projeto(projeto1)

    # Calculando o tempo de empresa
    print(f"{joao.nome} está na empresa há {joao.tempo_de_empresa()} dias.")

if __name__ == "__main__":
    main()
