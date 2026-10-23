class Lanche:
    taxa_entrega = 5

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def total(self):
        return self.preco + self.taxa_entrega

xtudo = Lanche("X-tudo", 30)
suco = Lanche("Suco", 8)

print(xtudo.total(), suco.total())               # 35 13

Lanche.taxa_entrega = 7
print(xtudo.total(), suco.total())               # 37 15

suco.taxa_entrega = 0
Lanche.taxa_entrega = 10
print(xtudo.total(), suco.total())               # 40 8
print(Lanche.taxa_entrega, suco.taxa_entrega)    # 10 0

print(f"chave: {xtudo.total()}-{suco.total()}-{Lanche.taxa_entrega}")    # 40-8-10