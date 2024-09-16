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
        self.carrinho = []
        self.total = 0
        
    def adicionar(self, produto):
        self.carrinho.append(produto)
    
    def remover(self, index):
        for id, item in enumerate(self.carrinho):
            if index <= len(self.carrinho):
                if index-1==id:
                    self.carrinho.pop(id)
                    return f"Item excluido com sucesso!"
            else:
                return f"Item não localizado!"
        
    def mostrar(self):
        if len(self.carrinho)>=1:
            for produto in self.carrinho: 
                print(produto)
                self.total += (produto.valor - produto.desconto()) * produto.quantidade
            return f"Valor total dos produtos: {self.total}"
        else:
            return f"Carinho Vazio!"
       
              
class Produto:
    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
    
    @abstractmethod
    def desconto():
        raise NotImplementedError("Desconto não implementado! ")
    
class Eletronicos(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
    
    def desconto(self):
        return self.valor * (10/100)
    
    def __str__(self):
        return f"Nome: {self.nome:<20} - Quantidade: {self.quantidade:<5}  {'unidades' if self.quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self.valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self.valor - self.desconto()) * self.quantidade:<5}"
    
class Moveis(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
        
    def desconto(self):
        return self.valor * (15/100)
        
    def __str__(self):
        return f"Nome: {self.nome:<20} - Quantidade: {self.quantidade:<5}  {'unidades' if self.quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self.valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self.valor - self.desconto()) * self.quantidade:<5}"
    
class Vestuario(Produto):
    def __init__(self, nome, quantidade, valor):
        super().__init__(nome=nome, quantidade=quantidade, valor=valor)  
    
    def desconto(self):
        return self.valor * (5/100)
        
    def __str__(self):
        return f"Nome: {self.nome:<20} - Quantidade: {self.quantidade:<5}  {'unidades' if self.quantidade!=1 else 'unidade ':<5} - Valor Original: R$: {self.valor:<7} - Desconto: R$: {self.desconto():<7} - Valor final: R$: {(self.valor - self.desconto()) * self.quantidade:<5}"
     
def main():
    celular = Eletronicos("Smile X1", 2, 1000.00)
    roupeiro = Moveis("Roupeiro Itati", 1, 500.00)
    carrinho = Carrinho_De_Compras()
    carrinho.adicionar(celular)
    carrinho.adicionar(roupeiro)
    #print(carrinho.remover(1))
    print(carrinho.mostrar())
    
if __name__=="__main__":
    main()