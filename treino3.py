# 1ª VA · Treino 3: o estacionamento do shopping
#
# 1. Veiculo: o __init__ recebe placa e horas e guarda as duas.
#    valor() RETORNA 6 reais por hora.
#    __str__ RETORNA, por exemplo:   ABC1D23: R$ 18.00
#    (no __str__, use self.valor(): cada filha tem o seu valor)
#
# 2. Moto é um Veiculo. Sobrescreva valor(): 3 reais por hora.
#
# 3. Caminhao é um Veiculo com um dado a mais: eixos.
#    O __init__ recebe placa, horas e eixos, entrega ao
#    super().__init__ o que é do pai e guarda os eixos.
#    valor() é o valor do pai (super().valor()) mais 10 reais
#    por eixo.
# Nenhum print dentro das classes.


class Veiculo:
    def __init__(self, placa, horas):
        self.placa = placa
        self.horas = horas

    def valor(self):
        return self.horas * 6

    def __str__(self):
        return f"{self.placa}: R$ {self.valor():.2f}"

class Moto(Veiculo):
    def valor(self):
        return self.horas * 3

class Caminhao(Veiculo):
    def __init__(self, placa, horas, eixos):
        super().__init__(placa, horas)
        self.eixos = eixos

    def valor(self):
        return super().valor() + self.eixos * 10


# ===== TESTE (não altere estas linhas) =====
carro = Veiculo("ABC1D23", 3)
moto = Moto("MOT0A12", 3)
caminhao = Caminhao("CAM9Z99", 2, 3)

print(carro)                  # ABC1D23: R$ 18.00
print(moto)                   # MOT0A12: R$ 9.00
print(caminhao)               # CAM9Z99: R$ 42.00
print(caminhao.eixos, caminhao.horas)    # 3 2

caixa = 0
for v in [carro, moto, caminhao, Moto("XYZ4E56", 1)]:
    caixa = caixa + v.valor()
print(f"Caixa do dia: R$ {caixa:.2f}")    # Caixa do dia: R$ 72.00
print(isinstance(caminhao, Veiculo))      # True