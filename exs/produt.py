class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self.preco      # faltou o _

p = Produto(2.5)
print(p.preco)
# RecursionError: maximum recursion depth exceeded

class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco     # a gaveta, com _

p = Produto(2.5)
print(p.preco)    # 2.5