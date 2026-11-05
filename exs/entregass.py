class Entrega:
    def __init__(self, destino, km):
        self.destino = destino
        self.km = km

    def preco(self):
        return 5 + 2 * self.km

    def __str__(self):
        return f"{self.destino}: R$ {self.preco():.2f}"

class Expressa(Entrega):
    def preco(self):
        return super().preco() * 2

class Agendada(Entrega):
    def __init__(self, destino, km, dia):
        super().__init__(destino, km)
        self.dia = dia

    def __str__(self):
        return f"{super().__str__()} no dia {self.dia}"

e1 = Entrega("Centro", 4)
e2 = Expressa("Setor Bueno", 4)
e3 = Agendada("Campinas", 10, "sábado")
print(e1)                 # Centro: R$ 13.00
print(e2)                 # Setor Bueno: R$ 26.00
print(e3)                 # Campinas: R$ 25.00 no dia sábado
print(f"chave: {e1.preco()}-{e2.preco()}-{e3.preco()}-{e3.dia}")    # 13-26-25-sábado