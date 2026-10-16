class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p = Produto("Caneta", 2.5)
p.preco = 3.0
print(p.preco * 10)    # 30.0