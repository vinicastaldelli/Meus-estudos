class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def de_texto(cls, texto):          # faltou o @classmethod
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))

bia = ContaPoupanca.de_texto("Bia;200")

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-05\poupanca.py", line 12, in <module>
#     bia = ContaPoupanca.de_texto("Bia;200")
# TypeError: ContaPoupanca.de_texto() missing 1 required positional argument: 'texto'