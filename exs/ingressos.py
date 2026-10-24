class Ingresso:
    def __init__(self, filme, preco):
        self.filme = filme
        self.preco = preco

    def valor(self):
        return self.preco

    def total(self, quantidade):
        return self.valor() * quantidade

    def __str__(self):
        return f"{self.filme}: R$ {self.valor():.2f}"

class MeiaEntrada(Ingresso):
    def valor(self):
        return self.preco / 2

class Vip(Ingresso):
    def valor(self):
        return super().valor() + 15

i1 = Ingresso("Duna", 30)
i2 = MeiaEntrada("Duna", 30)
i3 = Vip("Duna", 30)

print(i1.valor())     # 30
print(i2.valor())     # 15
print(i3.valor())     # 45
print(i2.total(2))    # 30
print(i3)             # Duna: R$ 45.00
print(f"chave: {i1.valor()}-{i2.valor()}-{i3.valor()}-{i2.total(2)}")    # 30-15.0-45-30.0