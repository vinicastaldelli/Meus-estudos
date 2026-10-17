class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo           # passa pelo setter

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("o saldo não pode ficar negativo")
        self._saldo = valor

conta = ContaBancaria("Ana", 100)
conta.saldo = 250
print(conta.saldo)        # 250
conta.saldo = -100
print(conta.saldo)        # não chega aqui

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\conta.py", line 19, in <module>
#     conta.saldo = -100
#     ^^^^^^^^^^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\conta.py", line 13, in saldo
#     raise ValueError("o saldo não pode ficar negativo")
# ValueError: o saldo não pode ficar negativo