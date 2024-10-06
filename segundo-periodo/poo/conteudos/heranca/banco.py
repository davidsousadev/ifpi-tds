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

class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo=0, percentual_imposto=0.0):
        super().__init__(numero, saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_Imposto(self):
        operacao = f"Calcular imposto na conta {self.numero}."
        if self.autenticar(operacao):
            imposto = self._saldo * self.percentual_imposto
            self._saldo -= imposto
            print(f"Imposto calculado e deduzido. Novo saldo: {self.saldo:.2f}")
        else:
            print("Operação cancelada.")

    def __str__(self):
        return f"ContaImposto Número: {self.numero}, Saldo: {self.saldo:.2f}, Percentual de Imposto: {self.percentual_imposto * 100:.2f}%"

if __name__ == "__main__":
    cc1 = ContaCorrente(101, 500)
    cc2 = ContaCorrente(102, 100)

    cp1 = ContaPoupanca(201, 1500, 0.05)
    cp2 = ContaPoupanca(202, 2000, 0.03)

    ci1 = ContaImposto(301, 3000, 0.10)
    ci2 = ContaImposto(302, 4000, 0.12)

    cc1.creditar(200)
    cc2.debitar(500)
    cc1.transferir(cc2, 100)

    cp1.renderJuros()
    cp2.renderJuros()

    ci1.calcula_Imposto()
    ci2.calcula_Imposto()

    print(cc1)
    print(cc2)
    print(cp1)
    print(cp2)
    print(ci1)
    print(ci2)
