class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

linhas = ["Ana;1000", "Bia;200", "Caio;50"]    # como chegam de uma planilha

contas = []
for linha in linhas:
    partes = linha.split(";")                              # estas duas linhas vão se repetir
    conta = ContaPoupanca(partes[0], float(partes[1]))     # em todo lugar que ler um texto
    contas.append(conta)

print(contas[1].titular, contas[1].saldo)    # Bia 200.0
print(len(contas))                           # 3