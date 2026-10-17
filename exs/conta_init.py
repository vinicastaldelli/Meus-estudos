class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo           # o setter roda aqui também

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("o saldo não pode ficar negativo")
        self._saldo = valor

try:
    conta2 = ContaBancaria("Bia", -50)
    print("conta criada")                  # não roda
except ValueError as erro:
    print("não criou:", erro)              # não criou: o saldo não pode ficar negativo

print(conta2.titular)
# NameError: name 'conta2' is not defined