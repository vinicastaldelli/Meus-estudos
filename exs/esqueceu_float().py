class ContaPoupanca:
    taxa = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], partes[1])    # faltou o float()

bia = ContaPoupanca.de_texto("Bia;200")
print(bia.saldo)                # 200   (parece certo, mas é o texto "200")
print(bia.saldo * bia.taxa)

# 200
# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-05\poupanca.py", line 15, in <module>
#     print(bia.saldo * bia.taxa)
#           ~~~~~~~~~~^~~~~~~~~~
# TypeError: can't multiply sequence by non-int of type 'float'