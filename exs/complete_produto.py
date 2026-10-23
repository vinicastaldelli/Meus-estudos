class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]), int(partes[2]))

    def valor_em_estoque(self):
        return self.preco * self.estoque

p1 = Produto("Caneta", 2.5, 10)
p2 = Produto.de_texto("Caderno;25;4")

print(p2.nome, p2.preco, p2.estoque)    # Caderno 25.0 4
print(p1.valor_em_estoque())            # 25.0
print(p2.valor_em_estoque())            # 100.0
print(f"chave: {p2.nome}-{p2.valor_em_estoque()}-{p1.valor_em_estoque()}")