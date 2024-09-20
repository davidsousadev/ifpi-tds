"""

Implemente um sistema simples de gerenciamento de uma loja. O sistema deve lidar com diferentes tipos de produtos . Cada tipo de produto terá suas próprias características específicas e seu próprio método de cálculo de desconto.
A loja pode vender vários produtos e deve ser possível aplicar um desconto diferenciado para cada tipo de produto. O sistema deve ser capaz de exibir a descrição completa de cada produto, incluindo o valor original, o valor do desconto aplicado e o valor final.
Além disso, você deve criar uma classe Carrinho de Compras  que pode conter múltiplos produtos (associação 1:N). O carrinho deve ser capaz de calcular o valor total da compra, aplicando os descontos corretamente.
Crie uma classe base Produto com os atributos comuns a todos os produtos (nome, preço) e um método calcular_desconto() que retorna o preço com desconto aplicado.Crie classes derivadas Eletronico, Movel e Vestuario que sobrescrevem o método calcular_desconto() para cada tipo de produto.
Eletrônicos: 10% de desconto.
Móveis: 15% de desconto.
Vestuário: 5% de desconto.
A classe Carrinho deve conter uma lista de produtos (associação 1:N) e um método para calcular o valor total da compra com os descontos. Implemente um polimorfismo (método polimórfico) para que o método calcular_desconto() seja chamado corretamente, independente do tipo de produto. Adicione um método na classe Carrinho que exiba a descrição completa de todos os produtos no carrinho, incluindo o valor original, desconto e o valor final.


"""

from abc import abstractmethod

class Carrinho_De_Compras:
    def __init__(self):
        self.__itens_carrinho = []
        
    def adicionar(self, produto):
        self.__itens_carrinho.append(produto)
        return f"Item: {produto.nome} adicionado com sucesso!"
    
    def remover(self, index):
        for id, item in enumerate(self.__itens_carrinho):
            if index <= len(self.__itens_carrinho):
                if index-1==id:
                    self.__itens_carrinho.pop(id)
                    return f"Item excluido com sucesso!"
            else:
                return f"Item não localizado!"
    
    def limpar_carrinho(self):
        self.__itens_carrinho = []
        return f"Carrinho limpo com sucesso!"
        
    def mostrar(self):
        if len(self.__itens_carrinho)>=1:
            print("-" * 63 + " Carrinho " + "-" * 63)
            print("-"*136)
            total = 0
            for produto in self.__itens_carrinho: 
                print(produto)
                total += (produto.valor - produto.desconto()) * produto.quantidade
            return f"Valor total dos produtos {'-' * 100 } R$: {total}"
        else:
            return f"Carinho Vazio!"
                  
class Produto:
    def __init__(self, nome, quantidade, valor):
        self._nome = nome
        self._quantidade = quantidade
        self._valor = valor
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @property
    def valor(self):
        return self._valor
    
    @abstractmethod
    def desconto():
        raise NotImplementedError("Desconto não implementado! ")
    
class Eletronicos(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
    
    def desconto(self):
        return self._valor * (10/100)
    
    def __str__(self):
        return f"Nome: {self._nome:<20} - Quantidade: {self._quantidade:<5}  {'unidades' if self._quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self._valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self._valor - self.desconto()) * self._quantidade:<5}"
    
class Moveis(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
        
    def desconto(self):
        return self._valor * (15/100)
        
    def __str__(self):
        return f"Nome: {self._nome:<20} - Quantidade: {self._quantidade:<5}  {'unidades' if self._quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self._valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self._valor - self.desconto()) * self._quantidade:<5}"
    
class Vestuario(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
    
    def desconto(self):
        return self._valor * (5/100)
        
    def __str__(self):
        return f"Nome: {self._nome:<20} - Quantidade: {self._quantidade:<5}  {'unidades' if self._quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self._valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self._valor - self.desconto()) * self._quantidade:<5}"
     
def main():
    # Objetos
    celular = Eletronicos("Smile X1", 2, 1000.00)
    televisao = Eletronicos("JH 70p", 7, 5400.00)
    roupeiro = Moveis("Roupeiro Itati", 1, 500.00)
    camisa = Vestuario("T-bob M", 3, 70.00)
    
    # Objeto carrinho
    carrinho = Carrinho_De_Compras()
    
    # Algumas operações
    print(carrinho.adicionar(celular))
    print(carrinho.adicionar(televisao))
    print(carrinho.adicionar(roupeiro))
    print(carrinho.adicionar(camisa))
    print(carrinho.remover(2))
    print(carrinho.mostrar())
    print(carrinho.limpar_carrinho())
    print(carrinho.mostrar())
if __name__=="__main__":
    main()