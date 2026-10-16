class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo        # o valor mora no _saldo

    @property
    def saldo(self):               # roda quando alguém LÊ conta.saldo
        return self._saldo

conta = ContaBancaria("Ana", 1000)
print(conta.saldo)                 # 1000   (sem parênteses)
print(conta.saldo + 50)            # 1050