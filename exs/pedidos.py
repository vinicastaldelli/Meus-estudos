class Pedido:
    def __init__(self, cliente, quantidade, preco):
        self.cliente = cliente
        self.quantidade = quantidade
        self.preco = preco

    def subtotal(self):
        if self.quantidade <= 0:
            raise ValueError(f"quantidade inválida: {self.quantidade}")
        return self.quantidade * self.preco

    def total(self):
        return self.subtotal() + 8    # não trata: deixa o erro subir

pedidos = [Pedido("Ana", 2, 45), Pedido("Caio", 0, 45), Pedido("Duda", 1, 40)]

for pedido in pedidos:
    try:
        print(pedido.cliente, "paga", pedido.total())
    except ValueError as erro:
        print(pedido.cliente, "não fechou:", erro)

# Ana paga 98
# Caio não fechou: quantidade inválida: 0
# Duda paga 48