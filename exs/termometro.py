class Termometro:
    def __init__(self, graus):
        self.graus = graus

    @property
    def graus(self):
        return self._graus

    @graus.setter
    def graus(self, valor):
        if valor < -50 or valor > 60:
            raise ValueError("Temperatura fora da faixa")
        self._graus = valor

t = Termometro(25)
print(t.graus)    # 25
t.graus = 300
# ValueError: Temperatura fora da faixa