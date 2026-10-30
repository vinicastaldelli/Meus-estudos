class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        if isinstance(outro, Ponto):
            return Ponto(self.x + outro.x, self.y + outro.y)
        return NotImplemented

    def __eq__(self, outro):
        if isinstance(outro, Ponto):
            return self.x == outro.x and self.y == outro.y
        return NotImplemented

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

coisas = [3, "3", [3], Ponto(3, 1)]

for c in coisas:
    print(c + c)                   # ?  (são 4 linhas)

p = Ponto(3, 1)
print(p + p == Ponto(6, 2))        # ?
print(p == "Ponto(3, 1)")          # ?
print(p)                           # ?
print(f"chave: {coisas[1] + coisas[1]}-{coisas[0] + coisas[0]}-{p + p == Ponto(6, 2)}-{p == 'Ponto(3, 1)'}")    # ?