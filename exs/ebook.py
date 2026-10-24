class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

class Ebook(Produto):
    def __init__(self, nome, preco, paginas):
        super().__init__(nome, preco)
        self.paginas = paginas

e1 = Ebook("Python na Prática", 39.9, 320)
e2 = Ebook("SQL Básico", 25, 140)

print(e1.etiqueta())
print(e2.etiqueta())
print(f"chave: {len(e2.nome)}-{e1.paginas + e2.paginas}-{e2.preco * 2}")