from consulta_medica import ConsultaMedica
from collections import defaultdict
from datetime import datetime

class Clinica:
    def __init__(self):
        self.consultas = []

    def nova_consulta(self):
        data_consulta = input("Digite a data da consulta (dd/mm/aaaa): ")
        paciente = input("Digite o nome do paciente: ")
        medico = input("Digite o nome do médico: ")
        try:
            consulta = ConsultaMedica(data_consulta, paciente, medico)
            self.consultas.append(consulta)
            print("\nConsulta agendada com sucesso!")
        except ValueError as e:
            print(e)

    def pagar_consulta(self):
        paciente = input("Digite o nome do paciente: ")
        consulta = self.buscar_consulta(paciente)
        if consulta:
            consulta.pago = True
            print("\nConsulta paga com sucesso!")
        else:
            print("\nConsulta não encontrada!")

    def cancelar_consulta(self):
        paciente = input("Digite o nome do paciente: ")
        consulta = self.buscar_consulta(paciente)
        if consulta:
            consulta.cancelado = True
            print("\nConsulta cancelada com sucesso!")
        else:
            print("\nConsulta não encontrada!")

    def agendar_retorno(self):
        paciente = input("Digite o nome do paciente: ")
        consulta = self.buscar_consulta(paciente)
        if consulta:
            try:
                consulta.agendar_retorno()
                print("\nRetorno agendado com sucesso!")
            except ValueError as e:
                print(e)
        else:
            print("\nConsulta não encontrada!")

    def relatorio_consultas(self):
        medico = input("Digite o nome do médico: ")
        consultas_realizadas = [consulta for consulta in self.consultas if consulta.medico == medico and consulta.pago and not consulta.cancelado]
        total_clientes = len(consultas_realizadas)
        total_recebido = total_clientes * 200
        print("\n------------------------------------------------------------")
        print(f"Relatório de consultas realizadas no mês pelo médico {medico}:")
        print(f"Total de clientes: {total_clientes}")
        print(f"Total recebido pelo médico: R${total_recebido}\n")
        for consulta in consultas_realizadas:
            print(consulta)

    def relatorio_faturamento(self):
        mes = int(input("Digite o mês desejado (1-12): "))
        consultas_pagadas = [consulta for consulta in self.consultas if consulta.pago and not consulta.cancelado and consulta.data_consulta.month == mes]
        total_pacientes = len(consultas_pagadas)
        total_faturado = total_pacientes * 300
        total_clinica = total_pacientes * 100
        print("\n------------------------------------------------------------")
        print(f"Relatório de faturamento da clínica:") 
        print(f"Mês {mes}:")
        print(f"Total de pacientes: {total_pacientes}")
        print(f"Total faturado: R${total_faturado}")
        print(f"Total para a clínica: R${total_clinica}\n")

    def buscar_consulta(self, paciente):
        for consulta in self.consultas:
            if consulta.paciente == paciente:
                return consulta
        return None
