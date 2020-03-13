from controller.files import Files
from controller.blacklist import Blacklist
from controller.validate import Validate

erros = []
success = []

try:
    fileController = Files()
    blacklistController = Blacklist()

    dataFiles = fileController.getFilesData()

    for file in dataFiles:
        for line, registro in enumerate(dataFiles[file]):
            try:
                data = registro.split(";")

                idMensagem = data[0]
                ddd = data[1]
                telefone = data[2]
                idBroker = fileController.getIdBroker(data[3])
                horarioAgendamento = data[4]
                mensagem = data[5]

                validateController = Validate(telefone, ddd, mensagem, horarioAgendamento)
                validateController.validateAll()

                if blacklistController.consultarTelefone(telefone):
                    raise Exception("[%s] -> Telefone na Blacklist: %s" % (file, telefone))

                success.append("[%s] -> %s;%s" % (file, idMensagem, idBroker))

            except Exception as err:
                erros.append("[%s] -> Linha[%s] -> %s" % (file, line + 1, err))
                continue

    print("Sucesso:")
    for line in success:
        print(line)

    print("\nErros:")
    for line in erros:
        print(line)

except Exception as err:
    print(err)
