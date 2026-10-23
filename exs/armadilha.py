class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

ana = ContaPoupanca("Ana", 1000)
bia = ContaPoupanca("Bia", 200)

ana.taxa = 0.10              # parece mudar a taxa, mas cria um atributo NOVO, só na ana
print(ana.taxa, bia.taxa)    # 0.1 0.05
print(ContaPoupanca.taxa)    # 0.05

ContaPoupanca.taxa = 0.07    # agora sim: mudou na classe
print(ana.taxa, bia.taxa)    # 0.1 0.07