class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo                # já passa pelo setter

    @property
    def saldo(self):                      # getter: roda quando alguém LÊ
        return self._saldo

    @saldo.setter
    def saldo(self, valor):               # setter: roda quando alguém GRAVA
        print(f"o setter recebeu {valor}")
        self._saldo = valor

conta = ContaBancaria("Ana", 1000)        # o setter recebeu 1000
conta.saldo = 1200                        # o setter recebeu 1200
print(conta.saldo)                        # 1200