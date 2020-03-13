import yaml
import os
import traceback


class Files:
    def __init__(self):
        self.configs = self.openConfig()
        self.dirFiles = 'files/'

    @staticmethod
    def openConfig():
        """
        Função para pegar as configurações no arquivo .yml
        :return:
        """
        try:
            with open('config/config.yml') as config:
                data = yaml.load(config, Loader=yaml.FullLoader)
                return data

        except Exception as err:
            raise Exception("Erro ao pegar configurações: %s" % err)

    def getFilesData(self):
        """
        Função utilizada para salvar todas as linhas dos arquivos em uma Lista
        :return:
        """
        try:
            data_arquivos = {}

            files = os.listdir(self.dirFiles)

            for file in files:
                with open(os.path.join(self.dirFiles, file)) as fileData:
                    data_arquivos[file] = fileData.readlines()

            return data_arquivos
        except Exception as err:
            raise Exception("[files] Erro ao pegar os regstros nos arquivos: %s \n%s" % (err, traceback.format_exc()))

    def getIdBroker(self, brokerFile):
        """
        Pesquisa a partir da configuração, qual o ID do broker em específico
        :param brokerFile:
        :return: ID do Broker
        """
        for broker in self.configs["Brokers"]:
            if brokerFile.lower() in [x.lower() for x in self.configs["Brokers"][broker]]:
                return broker

        raise Exception("Broker não encontrado: %s" % brokerFile)
