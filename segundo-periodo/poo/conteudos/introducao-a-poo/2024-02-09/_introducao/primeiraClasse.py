'''
Utilizando a linguagem python, implemente a classe e o objeto que você pensou na aula passada.
Dica: 
1.A classe tem que ter pelo menos um atributo mutável.
2. Os métodos devem ter relação com algum atributo mutável.
'''
import time



class computador:
    modelo=None
    marca=None
    cpu=None
    memoria_atual=0
    memoria_ram_max=None
    capacidade_hd=0
    capacidade_hd_max=None
    arquivos = {}
    quantidade_arquivos = 0      
    estado='desligado'
    
    def ligar(self):
        countdown_timer(6)
        self.estado = 'ligado'
    def desligar(self):
        self.estado = 'deligado'
    
    def criar_arquivo(self, nome_arquivo, tamanho):
        if self.estado == 'ligado':
            if self.capacidade_hd_max-tamanho > 0:
                self.capacidade_hd_max-=tamanho
                self.arquivos[self.quantidade_arquivos] = (nome_arquivo,tamanho)
                self.quantidade_arquivos +=1
                print(f"Arquivo de {tamanho} GB adicionado no HD.")
            else:
                print("Memoria Cheia!")
        else:
            print("Computador Desligado!")


        
    def listar_arquivos(self):
        if self.estado == 'ligado':
            for x in range(0,self.quantidade_arquivos):
                print(f"Nome: {self.arquivos[x][0]} | {self.arquivos[x][1]}")
            return f"{self.quantidade_arquivos} arquivos"
        else:
            return f"Computador Desligado!"
        

    def deletar_arquivo(self):
        if self.estado == 'ligado':
            nome_arquivo = str(input("Qual o nome do arquivo: ").strip())
            quantidade = 0
            for x in range(self.quantidade_arquivos):
                if self.arquivos[x][0]==nome_arquivo:
                    quantidade +=1
                    print(self.arquivos[x][0])
            if quantidade >= 2:
                opcao = input((f"Exite mais de um arquivo com esse nome: {nome_arquivo}\nDeseja apagar todos:\n 1 - Sim \n2 - Não ").strip())
                if opcao==1:    
                    for x in range(self.quantidade_arquivos):
                        if self.arquivos[x][0]==nome_arquivo:
                            self.capacidade_hd_max += self.arquivos[x][1]
                            self.quantidade_arquivos -= 1
                            self.arquivos.update(x = (None,None))
                    return f"Apagado com sucesso!!!"
                else:
                    return f"Operação cancelada!!!" 
            elif quantidade==1:
                for x in range(self.quantidade_arquivos):
                        if self.arquivos[x][0]==nome_arquivo:
                            self.capacidade_hd_max += self.arquivos[x][1]
                            self.quantidade_arquivos -= 1
                            self.arquivos.update(x = (None,None))
                return f"Apagado com sucesso!!!"
            else:
                return f"Arquivo {nome_arquivo} não encontrado!!!" 
        else:
            return f"Computador Desligado!"



def informacao(info):
    if info==1:
        return f"HD 1000 GB"
    elif info==2:
        return f"8GB"
    elif info==3:
         return f"I5"
    elif info==4:
        return f"Dell"
    elif info==5:
        return f"Inpirion 3360"
    elif info==6:
        return f"Ligando aguarde"
    
    


def countdown_timer(seconds):
    while seconds:
        print(informacao(seconds))
        time.sleep(2)
        seconds -= 1

while True:       
    ligar = int(input("Deseja ligar o computador Inpirion 3360:\n1-Sim \n2-Não\n"))

    if(ligar==1):
        dell_inspiron = computador()
        dell_inspiron.modelo = "Inpirion 3360"
        dell_inspiron.marca = "Dell"
        dell_inspiron.cpu = "I5"
        dell_inspiron.memoria_ram_max = "8GB"
        dell_inspiron.capacidade_hd_max = 1000 
        dell_inspiron.ligar()
        print(f"Computador {dell_inspiron.estado}.")
        while True:
            try:
                opcao = int(input("""
=============== MENU INICIAR ===============
Escolha uma opção:
1 - Desliga o computador
2 - Adicionar arquivo
3 - Status da capacidade do HD
4 - Listar arquivos
5 - Deletar arquivo
"""))
                if opcao==1:  
                    dell_inspiron.estado = 'desligado'
                    print(f"Computador {dell_inspiron.estado}.\n")
                    break
                elif opcao==2:
                    if dell_inspiron.estado == 'ligado':
                        nome = str(input("Digite nome do arquivo: ").strip())
                        tamanho = int(input("Digite o Tamanho do arquivo em GB: "))
                        dell_inspiron.criar_arquivo(nome, tamanho)
                    else:
                        print("Computador Desligado!")       
                elif opcao==3:
                    if dell_inspiron.estado == 'ligado':
                        print(f"Capacidade disponivel do HD está em {dell_inspiron.capacidade_hd_max} GB")
                    else:
                        print("Computador Desligado!")   
                elif opcao==4:

                    print(dell_inspiron.listar_arquivos())
                elif opcao==5:
                    print(dell_inspiron.deletar_arquivo())    
                else:
                    print("Opção invalida!")
            except:
                print(f"Erro na operação!!!")
    else:
        break