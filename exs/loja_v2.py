class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        if valor >= 0:
            self._preco = valor

p = Produto("Caneta", 2.5)
p.set_preco(3.0)              # linha reescrita
print(p.get_preco() * 10)     # 30.0   (linha reescrita)