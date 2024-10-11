from datetime import datetime

class Pessoa:
    def __init__(self, cpf, nome, endereco, fone, dt_nasc):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.dt_nasc = dt_nasc
        self.gato = None

    def adotar_Gato(self, gato):
        if self.idade() < 16:
            print(f"{self.nome} não pode adotar um gato porque tem menos de 16 anos.")
            return
        if self.gato is not None:
            print(f"{self.nome} já tem um gato.")
            return
        if gato.dono is not None:
            print(f"{gato.nome} já tem um dono.")
            return
        self.gato = gato
        gato.dono = self

    def idade(self):
        hoje = datetime.now()
        nascimento = datetime.strptime(self.dt_nasc, '%d/%m/%Y')
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

class Gato:
    def __init__(self, codigo, nome, dt_nasc, raca):
        self.codigo = codigo
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.raca = raca
        self.dono = None

    def cadastrar_dono(self, dono):
        if dono.idade() < 16:
            print(f"{dono.nome} não pode ser dono de um gato porque tem menos de 16 anos.")
            return
        if self.dono is not None:
            print(f"{self.nome} já tem um dono.")
            return
        if dono.gato is not None:
            print(f"{dono.nome} já tem um gato.")
            return
        self.dono = dono
        dono.gato = self

    def __str__(self):
        dono_nome = self.dono.nome if self.dono else "Sem dono"
        return (f"Nome do Gato: {self.nome}\n"
                f"Código: {self.codigo}\n"
                f"Data nascimento: {self.dt_nasc}\n"
                f"Meu dono: {dono_nome}")

# Execuções

# Execução 1
Joao = Pessoa('0980980989', 'João', 'rua 100', 86988761234, '01/01/2000')
Mimi = Gato(1, 'Mimi', '01/02/2023', 'SRD')
Joao.adotar_Gato(Mimi)
print(Mimi)

print("\n")

# Execução 2
Joao = Pessoa('0980980989', 'João', 'rua 100', 86988761234, '01/01/2000')
Mimi = Gato(1, 'Mimi', '01/02/2023', 'SRD')
Mimi.cadastrar_dono(Joao)
print(Mimi)

print("\n")

# Execução 3
Maria = Pessoa('0980980988', 'Maria', 'Av 100', 86988761235, '01/01/2009')
Jojo = Gato(2, 'Jojo', '01/02/2024', 'SRD')
Maria.adotar_Gato(Jojo)
print(Jojo)

print("\n")

# Execução 4
Maria = Pessoa('0980980988', 'Maria', 'Av 100', 86988761235, '01/01/2009')
Jojo = Gato(2, 'Jojo', '01/02/2024', 'SRD')
Jojo.cadastrar_dono(Maria)
print(Jojo)