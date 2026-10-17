class Cartao:
    def __init__(self, limite):
        self.limite = limite

    def pagar(self, valor):
        if valor > self.limite:
            raise ValueError("limite insuficiente")
        self.limite = self.limite - valor

class Maquininha:
    def __init__(self):
        self.aprovadas = 0
        self.atendimentos = 0

    def cobrar(self, cartao, valor):
        try:
            cartao.pagar(valor)
        except ValueError as erro:
            print("Recusado:", erro)
        else:
            print("Aprovado: R$", valor)
            self.aprovadas = self.aprovadas + 1
        finally:
            print("Tela inicial")
            self.atendimentos = self.atendimentos + 1

maquininha = Maquininha()
cartao = Cartao(100)
maquininha.cobrar(cartao, 30)
maquininha.cobrar(cartao, 90)
maquininha.cobrar(cartao, 70)
print(f"chave: {maquininha.aprovadas}-{maquininha.atendimentos}-{cartao.limite}")

# Aprovado: R$ 30
# Tela inicial
# Recusado: limite insuficiente
# Tela inicial
# Aprovado: R$ 70
# Tela inicial