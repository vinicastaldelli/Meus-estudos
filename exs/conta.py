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
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

conta = ContaBancaria("Ana", 100)
print(conta.saldo)    # 100
conta.saldo = -100
print("esta linha não roda")

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-03\conta.py", line 18, in <module>
#     conta.saldo = -100
#     ^^^^^^^^^^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-03\conta.py", line 13, in saldo
#     raise ValueError("Saldo não pode ser negativo")
# ValueError: Saldo não pode ser negativo