class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo        # _ na frente: "uso interno"

    def depositar(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor

    def ver_saldo(self):
        return self._saldo

conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
print(conta.ver_saldo())    # 1500

conta._saldo = -9999        # o Python deixa: o _ é só um aviso
print(conta.ver_saldo())    # -9999