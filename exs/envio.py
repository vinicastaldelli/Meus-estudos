def frete_fixo(peso):
    return 15

def frete_por_quilo(peso):
    return peso * 4

class Envio:
    def __init__(self, destino, peso, calcular_frete):
        self.destino = destino
        self.peso = peso
        self.calcular_frete = calcular_frete

    def frete(self):
        return self.calcular_frete(self.peso)

e1 = Envio("Goiânia", 3, frete_fixo)
e2 = Envio("Anápolis", 5, frete_por_quilo)

print(e1.destino, e1.frete())
print(e2.destino, e2.frete())
e2.peso = 6                      # a encomenda ficou mais pesada
print(f"chave: {e1.frete()}-{e2.frete()}-{e1.frete() + e2.frete()}")