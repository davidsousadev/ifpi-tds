from datetime import *
class cnh():
    def __init__(self, nome,rg,orgao_expeditor,cpf,data_de_nascimento,data_primeira_habilitacao,categoria,data_de_emissao,observacao):
        self.nome=nome
        self.rg=rg
        self.orgao_expeditor=orgao_expeditor
        self.cpf=cpf
        self.data_de_nascimento=data_de_nascimento
        self.primeira_habilitacao=data_primeira_habilitacao
        self.categoria=self.valida_categoria(categoria)
        self.data_de_emissao=data_de_emissao
        self.observacao=observacao

    def valida_categoria(self,categoria):
        categorias=['A','AB','AC','AD','AE','B','C','D','E']
        for x in categorias:
            if x==categoria:
                print(x)
                return categoria
            else:
                print(f"Categoria invalida")
    
    def alterar_categoria(self):
        nova_categoria = str(input("Digite a nova categoria: ").strip())
        self.categoria = nova_categoria
        
    
    def mudar_observacao(self):
        nova_observacao = str(input("Digite a nova observação: ").strip())
        self.observacao = nova_observacao


hab1 = cnh("Raissa Lopes","1525412","SSP",152525252,date(year=2005, month=3, day=10), date.today(), "B",date.today(),"SEM OBSERVAÇÃO")# objeto

hab2 = cnh("David Sousa","74525412","SSP",152205252,date(year=1996, month=3, day=26) , date.today(), "AB",date.today(),"SEM OBSERVAÇÃO")# objeto

hab1.alterar_categoria()

hab2.mudar_observacao()

print(hab1.categoria)