class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        cls(partes[0], float(partes[1]))    # faltou o return

bia = ContaPoupanca.de_texto("Bia;200")
print(bia.titular)

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-05\poupanca.py", line 14, in <module>
#     print(bia.titular)
#           ^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'titular'