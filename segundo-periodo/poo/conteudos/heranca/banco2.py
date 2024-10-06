import getpass

class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self._saldo = saldo
        self._senha = getpass.getpass(f"Defina uma senha para a conta {self.numero}: ")

    def autenticar(self, operacao):
        print(operacao)
        senha = getpass.getpass("Digite a senha para continuar: ")
        if senha == self._senha:
            return True
        else:
            print("Senha incorreta.")
            return False

    def creditar(self, valor):
        operacao = f"Creditar {valor:.2f} na conta {self.numero}."
        if self.autenticar(operacao):
            self._saldo += valor
            print(f"Valor creditado com sucesso! Novo saldo: {self.saldo:.2f}")
        else:
            print("Operação cancelada.")

    def debitar(self, valor):
        operacao = f"Debitar {valor:.2f} da conta {self.numero}."
        if self.autenticar(operacao):
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Valor debitado com sucesso! Novo saldo: {self.saldo:.2f}")
            else:
                print("Saldo insuficiente para debitar.")
        else:
            print("Operação cancelada.")

    @property
    def saldo(self):
        return self._saldo

    def transferir(self, conta_destino, valor):
        operacao = f"Transferir {valor:.2f} da conta {self.numero} para a conta {conta_destino.numero}."
        if self.autenticar(operacao):
            if valor <= self._saldo:
                self.debitar(valor)
                conta_destino.creditar(valor)
                print(f"Transferência de {valor:.2f} para conta {conta_destino.numero} realizada com sucesso!")
            else:
                print("Saldo insuficiente para transferir.")
        else:
            print("Operação cancelada.")

    def __str__(self):
        return f"ContaCorrente Número: {self.numero}, Saldo: {self.saldo:.2f}"

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo=0, taxa_juros=0.0):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros

    def renderJuros(self):
        operacao = f"Aplicar juros na conta {self.numero}."
        if self.autenticar(operacao):
            self._saldo += self._saldo * self.taxa_juros
            print(f"Juros aplicados! Novo saldo: {self.saldo:.2f}")
        else:
            print("Operação cancelada.")

    def __str__(self):
        return f"ContaPoupanca Número: {self.numero}, Saldo: {self.saldo:.2f}, Taxa de Juros: {self.taxa_juros * 100:.2f}%"

class ContaEspecial(ContaCorrente):
    def __init__(self, numero, saldo=0, limite=1000):
        super().__init__(numero, saldo)
        self.limite = limite

    def debitar(self, valor):
        operacao = f"Debitar {valor:.2f} da conta {self.numero} com limite especial."
        if self.autenticar(operacao):
            if valor <= self._saldo + self.limite:
                self._saldo -= valor
                print(f"Valor debitado com sucesso! Novo saldo: {self.saldo:.2f}")
            else:
                print("Saldo insuficiente, mesmo considerando o limite.")
        else:
            print("Operação cancelada.")

    def __str__(self):
        return f"ContaEspecial Número: {self.numero}, Saldo: {self.saldo:.2f}, Limite: {self.limite:.2f}"

class Banco:
    def __init__(self):
        self.valor_total = 0
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        self.valor_total += conta.saldo

    def mostrar_valor_total(self):
        valor_total = 0
        for conta in self.contas:
            valor_total += conta.saldo
        print(f"\nValor atual total de todas as contas do banco: {valor_total:.2f}\nValor inicial total de todas as contas do banco: {self.valor_total:.2f}")

if __name__ == "__main__":
    cc1 = ContaCorrente(123, 500)
    cp1 = ContaPoupanca(321, 1500, 0.05)
    ce1 = ContaEspecial(777, 1000, 2000)

    banco = Banco()

    banco.adicionar_conta(cc1)
    banco.adicionar_conta(cp1)
    banco.adicionar_conta(ce1)
    
    cc1.creditar(300)
    cp1.debitar(200)
    cc1.transferir(ce1, 100)
    cp1.renderJuros()
    ce1.debitar(5000)
     
    print(cc1)
    print(cp1)
    print(ce1)
    banco.mostrar_valor_total()