class ContaPoupanca:
    taxa = 0.05                  # atributo de CLASSE: um só, para todas as contas

    def __init__(self, titular, saldo):
        self.titular = titular   # atributos de instância: cada conta tem o seu
        self.saldo = saldo

    def render(self):
        self.saldo = self.saldo + self.saldo * self.taxa

ana = ContaPoupanca("Ana", 1000)
bia = ContaPoupanca("Bia", 200)

print(ContaPoupanca.taxa)        # 0.05
print(ana.taxa, bia.taxa)        # 0.05 0.05

ana.render()
bia.render()
print(ana.saldo, bia.saldo)      # 1050.0 210.0

ContaPoupanca.taxa = 0.10        # mudou na classe: vale para todas
print(ana.taxa, bia.taxa)        # 0.1 0.1