class Volume:
    def __init__(self, nivel):
        self.nivel = nivel                 # já passa pelo setter

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        if valor > 100:
            valor = 100                    # passou do máximo: vira o máximo
        elif valor < 0:
            valor = 0                      # abaixo do mínimo: vira o mínimo
        self._nivel = valor                # guarda uma vez só, no fim

v = Volume(50)
v.nivel = 150
print(v.nivel)                 # 100
v.nivel = -20
print(v.nivel)                 # 0
print("o programa segue")      # o programa segue