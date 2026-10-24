class Animal:
    def __init__(self, nome, patas):
        self.nome = nome
        self.patas = patas

    def apresentar(self):
        return f"{self.nome} tem {self.patas} patas"

class Cachorro(Animal):
    def latir(self):
        return f"{self.nome}: au au"

class Galinha(Animal):
    pass

rex = Cachorro("Rex", 4)
pintada = Galinha("Pintada", 2)

print(rex.apresentar())             # Rex tem 4 patas
print(pintada.apresentar())         # Pintada tem 2 patas
print(rex.latir())                  # Rex: au au
print(rex.patas + pintada.patas)    # 6
print(f"chave: {pintada.nome}-{pintada.patas}-{rex.patas + pintada.patas}")    # Pintada-2-6