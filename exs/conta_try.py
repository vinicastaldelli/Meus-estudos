class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("o saldo não pode ficar negativo")
        self._saldo = valor

conta = ContaBancaria("Ana", 100)

for novo in [250, -100, 80]:
    try:
        conta.saldo = novo
        print("saldo agora:", conta.saldo)
    except ValueError as erro:
        print("recusado:", erro)
        print("continua:", conta.saldo)

# saldo agora: 250
# recusado: o saldo não pode ficar negativo
# continua: 250
# saldo agora: 80