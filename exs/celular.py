class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Bateria:
    def __init__(self, carga):
        self.carga = carga

class Celular:
    def __init__(self, modelo, carga, dono):
        self.modelo = modelo
        self.dono = dono                  # associação: recebe pronto
        self.bateria = Bateria(carga)     # composição: cria aqui dentro

    def usar(self, minutos):
        self.bateria.carga = self.bateria.carga - minutos

bia = Pessoa("Bia")
cel1 = Celular("Moto", 80, bia)
cel2 = Celular("Galaxy", 50, bia)

cel1.usar(30)
b = cel2.bateria
cel2.usar(10)
bia.nome = "Beatriz"

print(cel1.bateria.carga)               # 50
print(b.carga)                          # 40
print(cel2.dono.nome)                   # Beatriz
print(cel1.bateria == cel2.bateria)     # False
print(f"chave: {cel1.bateria.carga}-{b.carga}-{cel2.dono.nome}")    # 50-40-Beatriz