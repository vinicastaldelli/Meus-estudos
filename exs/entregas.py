class Moto:
    def __init__(self, km):
        self.km = km

    def custo(self):
        return 5 + self.km

class Carro:
    def __init__(self, km):
        self.km = km

    def custo(self):
        return 10 + self.km * 2

class Bicicleta:
    def __init__(self, km):
        self.km = km

    def custo(self):
        return 2 + self.km

class Drone:
    def __init__(self, km):
        self.km = km

    def custo(self):
        return 20 + self.km * 3

entregas = [Moto(4), Carro(9), Bicicleta(3), Drone(5)]

total = 0
for e in entregas:
    total = total + e.custo()

print(f"chave: {len(entregas)}-{total}")