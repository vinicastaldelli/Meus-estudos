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
        return self.subtotal() + 8    # 8 reais de entrega

pedido = Pedido("Caio", 0, 45)
print(pedido.total())

# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\pedido.py", line 16, in <module>
#     print(pedido.total())
#           ~~~~~~~~~~~~^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\pedido.py", line 13, in total
#     return self.subtotal() + 8    # 8 reais de entrega
#            ~~~~~~~~~~~~~^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\pedido.py", line 9, in subtotal
#     raise ValueError(f"quantidade inválida: {self.quantidade}")
# ValueError: quantidade inválida: 0