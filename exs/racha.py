class Pedido:
    def __init__(self, quantidade, preco):
        self.quantidade = quantidade
        self.preco = preco

    def subtotal(self):
        if self.quantidade <= 0:
            raise ValueError("pedido vazio")
        return self.quantidade * self.preco

    def por_pessoa(self, pessoas):
        return self.subtotal() / pessoas

def rachar(pedido, pessoas):
    try:
        valor = pedido.por_pessoa(pessoas)
        print("cada um paga", valor)
        return "ok"
    except ZeroDivisionError:
        print("ninguém para pagar")
        return "zero"
    except ValueError as erro:
        print("problema:", erro)
        return "vazio"

r1 = rachar(Pedido(3, 20), 2)     # ?
r2 = rachar(Pedido(3, 20), 0)     # ?
r3 = rachar(Pedido(0, 50), 0)     # ?
print(f"chave: {r1}-{r2}-{r3}")   # ?