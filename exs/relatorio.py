class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"

def pegar_preco(produto):
    return produto.preco

produtos = [Produto("Camiseta", 59.9), Produto("Caneca", 35), Produto("Boné", 42)]

baratos = sorted(produtos, key=pegar_preco)
caro = max(produtos, key=lambda p: p.preco)
total = sum([p.preco for p in produtos])

print(baratos)      # [Produto('Caneca', 35), Produto('Boné', 42), Produto('Camiseta', 59.9)]
print(caro.nome)    # Camiseta
print(total)        # 136.9

print(f"chave: {baratos[0].preco}-{caro.preco - baratos[0].preco}-{total - caro.preco}")