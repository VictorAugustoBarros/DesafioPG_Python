from datetime import datetime
from controller.files import Files


class Validate:
    def __init__(self, telefone, DDD, mensagem, horarioAgendamento):
        self.DDD = DDD
        self.telefone = telefone
        self.mensagem = mensagem
        self.horarioAgendamento = self.convertStringtoDate(horarioAgendamento)
        self.envios = {}
        self.config = Files().confi

    def validateTelefone(self):

        """
        Função para validação específica do Telefone
        :return:
        """
        telefoneSize = len(self.telefone)

        if int(self.DDD) not in self.config["DDD"]:
            raise Exception("[Telefone] DDD inválido no Brasil: %s" % self.DDD)

        if len(self.DDD) > 2:
            raise Exception("[Telefone] Tamanho de DDD inválido: %s" % self.DDD)

        if not int(self.telefone[0]) == 9:
            raise Exception("[Telefone] Inicio do telefone inválido: %s " % self.telefone)

        if int(self.telefone[1]) < 6:
            raise Exception("[Telefone] Segundo dígito menor que 6: %s " % self.telefone)

        if not telefoneSize == 9:
            raise Exception("[Telefone] Tamanho inválido: %s " % self.telefone)

        if int(self.DDD) == 11:
            raise Exception("[Telefone] DDD bloqueado: [%s] São Paulo" % self.DDD)

        if self.telefone in self.envios.keys() and self.horarioAgendamento > self.envios[self.telefone]:
            raise Exception("[Telefone] Já foi enviada uma mensagem para esse número : %s" % self.telefone)

        self.envios[self.telefone] = self.horarioAgendamento.strftime("%H:%M:%S")

    def validateMessage(self):
        """
        Função para validação específica da Mensagem
        :return:
        """
        if len(self.mensagem) > 140:
            raise Exception("Mensagem inválida: excede 140 caracteres")

    def validateHorario(self):
        """
        Função para validação específica do Horário
        :return:
        """
        if self.horarioAgendamento.hour > 19:
            raise Exception("Horário agendamento inválido: horário [%s] acima das 19:59:59" % self.horarioAgendamento)

    @staticmethod
    def convertStringtoDate(date):
        """
        Converte a data String para Datetime
        :param date:
        :return: Data no formato Datetime
        """
        try:
            return datetime.strptime(date, '%H:%M:%S')
        except Exception as err:
            raise Exception("Horário agendamento inválido [%s]: %s" % (date, err))

    def validateAll(self):
        """
        Percorre todas as validações necessárias
        :return:
        """
        self.validateTelefone()
        self.validateMessage()
        self.validateHorario()
