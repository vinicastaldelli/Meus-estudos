class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def get_saldo(self):           # getter: quem lê
        return self._saldo

    def set_saldo(self, valor):    # setter: quem grava, e confere antes
        if valor < 0:
            print("Recusado: saldo não pode ser negativo")
        else:
            self._saldo = valor

conta = ContaBancaria("Ana", 1000)
conta.set_saldo(-500)                      # Recusado: saldo não pode ser negativo
print(conta.get_saldo())                   # 1000
conta.set_saldo(conta.get_saldo() + 50)
print(conta.get_saldo())                   # 1050