# 1ª VA · Treino 2: o cartão de transporte
#
# Escreva a classe CartaoTransporte:
# - o __init__ recebe titular e saldo. Guarda o titular e grava o
#   saldo com self.saldo = saldo, para passar pelo setter;
# - saldo é uma property: o getter RETORNA self._saldo;
# - o setter recusa valor negativo com
#       raise ValueError("saldo não pode ser negativo")
#   e só depois de conferir guarda em self._saldo;
# - pagar_passagem() tira 5 reais do saldo, gravando pelo setter
#   (self.saldo = ...). Sem saldo, o setter recusa sozinho.
# Nenhum print dentro da classe.


class CartaoTransporte:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("saldo não pode ser negativo")
        self._saldo = valor

    def pagar_passagem(self):
        self.saldo = self.saldo - 5

# ===== TESTE (não altere estas linhas) =====
cartao = CartaoTransporte("Ana", 12)
print(cartao.saldo)           # 12
cartao.pagar_passagem()
print(cartao.saldo)           # 7

try:
    cartao.saldo = -3
except ValueError as erro:
    print("recusado:", erro)  # recusado: saldo não pode ser negativo
print(cartao.saldo)           # 7

try:
    cartao.pagar_passagem()
    cartao.pagar_passagem()
except ValueError as erro:
    print("catraca:", erro)   # catraca: saldo não pode ser negativo
print(cartao.saldo)           # 2

try:
    CartaoTransporte("Bia", -10)
    criado = "sim"
except ValueError:
    criado = "não"
print("criado:", criado)      # criado: não