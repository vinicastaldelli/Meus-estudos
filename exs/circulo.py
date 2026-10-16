class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @property
    def area(self):                    # calculada na hora, a cada leitura
        return 3.14 * self._raio * self._raio

c = Circulo(2)
print(c.raio, c.area)    # 2 12.56
c.area = 50
# AttributeError: property 'area' of 'Circulo' object has no setter