class Carteira:
    def __init__(self, saldo):
        self.saldo = saldo

    def gastar(self, valor):
        # self.saldo = self.saldo - valor
        # if self.saldo < 0:
        #     raise ValueError("saldo insuficiente")
        if valor > self.saldo:
            raise ValueError("saldo insuficiente")
        self.saldo = self.saldo - valor
        return self.saldo

carteira = Carteira(100)
negadas = 0

for valor in [30, 80, 50, 40]:
    try:
        print("compra:", valor)
        restante = carteira.gastar(valor)
        print("restam:", restante)
    except ValueError as erro:
        print("negada:", erro)
        negadas = negadas + 1

print(carteira.saldo)
print(negadas)
print(f"chave: {carteira.saldo}-{negadas}")