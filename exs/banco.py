class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"tem R$ {self.saldo}, pediu R$ {valor}")
        self.saldo = self.saldo - valor

conta = ContaBancaria("Ana", 100)
conta.sacar(30)
print(conta.saldo)    # 70
conta.sacar(500)

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\banco.py", line 17, in <module>
#     conta.sacar(500)
#     ~~~~~~~~~~~^^^^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\banco.py", line 11, in sacar
#     raise SaldoInsuficienteError(f"tem R$ {self.saldo}, pediu R$ {valor}")
# SaldoInsuficienteError: tem R$ 70, pediu R$ 500

class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("o saque precisa ser maior que zero")
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"tem R$ {self.saldo}, pediu R$ {valor}")
        self.saldo = self.saldo - valor

conta = ContaBancaria("Ana", 100)

for valor in [30, -10, 500, 70]:
    try:
        conta.sacar(valor)
    except ValueError as erro:
        print("valor inválido:", erro)
    except SaldoInsuficienteError as erro:
        print("sem saldo:", erro)
    else:
        print("sacou", valor, "e sobrou", conta.saldo)

# sacou 30 e sobrou 70
# valor inválido: o saque precisa ser maior que zero
# sem saldo: tem R$ 70, pediu R$ 500
# sacou 70 e sobrou 0class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("o saque precisa ser maior que zero")
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"tem R$ {self.saldo}, pediu R$ {valor}")
        self.saldo = self.saldo - valor

conta = ContaBancaria("Ana", 100)

for valor in [30, -10, 500, 70]:
    try:
        conta.sacar(valor)
    except ValueError as erro:
        print("valor inválido:", erro)
    except SaldoInsuficienteError as erro:
        print("sem saldo:", erro)
    else:
        print("sacou", valor, "e sobrou", conta.saldo)

# sacou 30 e sobrou 70
# valor inválido: o saque precisa ser maior que zero
# sem saldo: tem R$ 70, pediu R$ 500
# sacou 70 e sobrou 0