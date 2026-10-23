class ContaPoupanca:
    taxa = 0.05
    total_contas = 0

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        ContaPoupanca.total_contas = ContaPoupanca.total_contas + 1

    @classmethod
    def de_texto(cls, texto):          # 1. construtor alternativo
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))

    @classmethod
    def mudar_taxa(cls, nova):         # 2. muda o que é de TODAS as contas
        cls.taxa = nova

    @classmethod
    def quantas(cls):                  # 3. lê o contador da classe
        return cls.total_contas

ana = ContaPoupanca("Ana", 1000)
bia = ContaPoupanca.de_texto("Bia;200")

ContaPoupanca.mudar_taxa(0.06)
print(ana.taxa, bia.taxa)            # 0.06 0.06
print(ContaPoupanca.quantas())       # 2