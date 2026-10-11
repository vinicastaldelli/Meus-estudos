# Aula 02 · Exercício 08 (casa, desafio): Pizza e Carrinho
#
# Pizza: o __init__ recebe sabor e preco. Só __repr__: Pizza('Calabresa', 45)
# Carrinho: nasce com self.pizzas = [] (lista vazia).
#   adicionar(pizza)  coloca a pizza na lista.
#   total()           RETORNA a soma dos preços, usando um for.
#   mais_cara()       RETORNA o objeto Pizza mais caro, usando um for.
#                     Se o carrinho estiver vazio, retorna None.
#   __str__           retorna, por exemplo: Carrinho: 3 pizzas, total R$ 132.50
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class Pizza:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco

    def __repr__(self):
        return f"Pizza('{self.sabor}', {self.preco})"

class Carrinho:
    def __init__(self):
        self.pizzas = []

    def adicionar(self, pizza):
        self.pizzas.append(pizza)

    def total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.preco
        return total

    def mais_cara(self):
        if not self.pizzas:
            return None
        pizza_mais_cara = self.pizzas[0]
        for pizza in self.pizzas[1:]:
            if pizza.preco > pizza_mais_cara.preco:
                pizza_mais_cara = pizza
        return pizza_mais_cara

    def __str__(self):
        return f"Carrinho: {len(self.pizzas)} pizzas, total R$ {self.total():.2f}"

p1 = Pizza('Calabresa', 75)
p2 = Pizza('Mussarela', 65)
c1 = Carrinho()
c1.adicionar(p1)
c1.adicionar(p2)

print(p1)
print(p2)
print(c1)
print(f"Total: R$ {c1.total():.2f}")
print(f"Pizza mais cara: {c1.mais_cara()}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# Pizza('Calabresa', 75)
# Pizza('Mussarela', 65)
# Carrinho: 2 pizzas, total R$ 140.00
# Total: R$ 140.00
# Pizza mais cara: Pizza('Calabresa', 75)