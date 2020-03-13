import requests


class Blacklist:
    def __init__(self):
        self.url = "https://front-test-pg.herokuapp.com/blacklist/"
        self.telefonesBlacklist = self.getAllTelefones()

    def getAllTelefones(self):
        """
        Consulta a API e retorna todos os telefones cadastrados
        :return: todos os telefones encontrados na requisição
        """
        r = requests.get(url=self.url)
        return r.json()

    def consultarTelefone(self, telefone):
        """
        Consulta se o telefone está cadastrado na Blacklist a partir da Lista obtida previamente
        :param telefone:
        :return: True -> Telefone na Blacklist / False -> Telefone OK
        """
        for registro in self.telefonesBlacklist:
            if registro["phone"] == telefone:
                return True
        return False
