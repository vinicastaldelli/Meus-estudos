class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @classmethod
    def de_texto(cls, texto):                     # cls recebe a própria classe
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))   # cls(...) é o mesmo que ContaPoupanca(...)

ana = ContaPoupanca("Ana", 1000)              # o construtor de sempre
bia = ContaPoupanca.de_texto("Bia;200")       # o construtor alternativo

print(bia.titular, bia.saldo)    # Bia 200.0
print(bia.taxa)                  # 0.05

contas = []
for linha in ["Caio;50", "Duda;300"]:
    contas.append(ContaPoupanca.de_texto(linha))    # uma linha só, em qualquer lugar
print(contas[1].titular, contas[1].saldo)    # Duda 300.0