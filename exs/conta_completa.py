class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular                  # só leitura: sem setter
        self.saldo = saldo                       # nasce passando pelo setter

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):                             # getter: quem lê
        return self._saldo

    @saldo.setter
    def saldo(self, valor):                      # setter: quem grava
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")    # recusa
        self._saldo = valor                      # guarda no _saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito tem que ser positivo")
        self.saldo = self.saldo + valor          # pelo setter

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Saque tem que ser positivo")
        self.saldo = self.saldo - valor          # saque grande demais: o setter recusa

    def __str__(self):
        return f"Conta de {self.titular} | saldo R$ {self.saldo:.2f}"

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
conta.sacar(30)
print(conta)            # Conta de Ana | saldo R$ 120.00
print(conta.saldo)      # 120

# Cada linha abaixo, se rodasse, pararia o programa:
# conta.sacar(500)        ValueError: Saldo não pode ser negativo
# conta.sacar(-100)       ValueError: Saque tem que ser positivo
# conta.saldo = -1        ValueError: Saldo não pode ser negativo
# conta.titular = "Bia"   AttributeError: property 'titular' of 'ContaBancaria' object has no setter