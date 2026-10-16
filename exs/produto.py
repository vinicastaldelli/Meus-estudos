class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco                 # passa pelo setter

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

p = Produto("Caneta", 2.5)
print(p.preco)       # 2.5
p.preco = 4
print(p.preco)       # 4
print(f"chave: {p.nome}-{p.preco * 3}-{Produto('Lápis', 0.5).preco * 4}")