class Quadrado:
    def __init__(self, lado):
        self._lado = lado

    @property
    def lado(self):
        return self._lado

    @property
    def area(self):
        return self._lado * self._lado

    def dobrar(self):
        self._lado = self._lado * 2

q = Quadrado(3)
print(q.lado, q.area)     # 3 9
q.dobrar()
print(q.lado, q.area)     # 6 36
print(q.area + 1)         # 37
print(f"chave: {q.lado}-{q.area}-{q.area + 1}")    # 6-36-37