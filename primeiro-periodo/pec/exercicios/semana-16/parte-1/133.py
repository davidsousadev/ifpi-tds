# Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os dados de todos os contatos do usuário (nome, cidade, estado, telefone) de forma que a agenda fique completa e por fim imprima todos os contatos.



def adicionar_contato():
    agenda = {}
    tamanho_agenda = int(input())
    id  = 0
    for i in range(tamanho_agenda):
        nome = str(input().strip())
        cidade = str(input().strip())
        estado = str(input().strip())
        telefone = str(input().strip())
        id += 1
        agenda[id] = {
            "Nome": nome,
            "Cidade": cidade,
            "Estado": estado,
            "Telefone": telefone
        }
    return agenda


    
def main():
    agenda = adicionar_contato()
    for id, info in agenda.items():
        citiEstado = f"{info['Cidade']}({info['Estado']})"
        print("{:<25}{:<30}{:<0}".format(info['Nome'], citiEstado, info['Telefone']))
  
  
            
if __name__ =='__main__':
	main()