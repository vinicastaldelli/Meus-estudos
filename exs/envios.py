class Envio:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

    def preco(self):
        return 10 + self.peso * 2

    def prazo(self):
        return 5

class Expresso(Envio):
    def preco(self):
        return super().preco() * 2

    def prazo(self):
        return 1

class Retirada(Envio):
    def preco(self):
        return 0

envios = [Envio("Anápolis", 3), Expresso("Anápolis", 3), Retirada("Goiânia", 10), Expresso("Trindade", 1)]

total = 0
maior_prazo = 0
for e in envios:
    total = total + e.preco()
    if e.prazo() > maior_prazo:
        maior_prazo = e.prazo()

print(envios[1].preco(), envios[2].prazo())    # 32 5
print(total)                                   # 72
print(maior_prazo)                             # 5
print(f"chave: {envios[1].preco()}-{envios[2].prazo()}-{total}-{maior_prazo}")    # 32-5-72-5