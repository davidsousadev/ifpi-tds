from datetime import datetime, timedelta, date

class ConsultaMedica:
    def __init__(self, data_consulta, paciente, medico):
        self.data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()
        if self.data_consulta <= date.today() or self.data_consulta.weekday() in [5, 6]:
            raise ValueError("A data da consulta deve ser maior que a data atual e não pode cair em um final de semana.")
        self._data_retorno = None
        self._pago = False
        self._cancelado = False
        self.paciente = paciente
        self.medico = medico

    @property
    def data_consulta(self):
        return self._data_consulta

    @data_consulta.setter
    def data_consulta(self, value):
        self._data_consulta = value

    @property
    def data_retorno(self):
        return self._data_retorno

    @data_retorno.setter
    def data_retorno(self, value):
        if self.pago:
            self._data_retorno = value
        else:
            raise ValueError("Não é possível agendar retorno para consulta não paga.")

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, value):
        self._paciente = value

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, value):
        self._medico = value

    @property
    def pago(self):
        return self._pago

    @pago.setter
    def pago(self, value):
        self._pago = value

    @property
    def cancelado(self):
        return self._cancelado

    @cancelado.setter
    def cancelado(self, value):
        self._cancelado = value

    def agendar_retorno(self):
        if self.pago:
            data_retorno = self.data_consulta + timedelta(days=30)
            while data_retorno.weekday() in [5, 6]:
                data_retorno += timedelta(days=1)
            self.data_retorno = data_retorno
        else:
            raise ValueError("A consulta deve ser paga antes de agendar um retorno.")

    def __str__(self):
        return (f"Consulta Médica:\n" 
                f"Data da Consulta: {self.data_consulta}\n"
                f"Paciente: {self.paciente}\n"
                f"Médico: {self.medico}\n"
                f"Pago: {'Sim' if self.pago else 'Não'}\n"
                f"Cancelado: {'Sim' if self.cancelado else 'Não'}\n"
                f"Data de Retorno: {self.data_retorno if self.data_retorno else 'Data de retorno não agendada!'}")


