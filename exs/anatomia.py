class SaldoInsuficienteError(Exception):        # erro com o nome do sistema
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo                      # passa pelo setter

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:                           # quem detecta...
            raise ValueError("saldo negativo")  # ...levanta (raise)
        self._saldo = valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("saque precisa ser maior que zero")
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"faltam R$ {valor - self.saldo}")
        self.saldo = self.saldo - valor

conta = ContaBancaria("Ana", 100)

for valor in [40, 0, 90]:
    try:                                        # quem sabe o que fazer: try
        conta.sacar(valor)                      # só a linha que pode falhar
    except ValueError as erro:                  # um except por tipo
        print("inválido:", erro)
    except SaldoInsuficienteError as erro:
        print("recusado:", erro)
    else:                                       # só se deu certo
        print("sacou", valor)
    finally:                                    # sempre, com erro ou sem
        print("saldo:", conta.saldo)

# sacou 40
# saldo: 60
# inválido: saque precisa ser maior que zero
# saldo: 60
# recusado: faltam R$ 30
# saldo: 60