class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo       # __ na frente: o Python troca o nome

    def ver_saldo(self):
        return self.__saldo        # aqui dentro, o nome curto funciona

conta = ContaBancaria("Ana", 1000)
print(conta.ver_saldo())              # 1000
print(conta._ContaBancaria__saldo)    # 1000   (o nome que o Python criou)
print(conta.__saldo)
# AttributeError: 'ContaBancaria' object has no attribute '__saldo'. Did you mean: 'ver_saldo'?