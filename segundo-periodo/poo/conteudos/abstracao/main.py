from clinica import Clinica

def main():
    clinica = Clinica()
    
    while True:
        print("\n --------------- Menu Principal --------------- ")
        print("1 - Nova consulta (agendamento)")
        print("2 - Pagar Consulta")
        print("3 - Cancelar consulta")
        print("4 - Agendar retorno")
        print("5 - Relatório de consultas realizadas no mês por médico")
        print("6 - Relatório de faturamento da Clínica por mês")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        
        match opcao:
            case 1:
                clinica.nova_consulta()
            case 2:
                clinica.pagar_consulta()
            case 3:
                clinica.cancelar_consulta()
            case 4:
                clinica.agendar_retorno()
            case 5:
                clinica.relatorio_consultas()
            case 6:
                clinica.relatorio_faturamento()
            case 0:
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
