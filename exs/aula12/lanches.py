from pathlib import Path

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def de_linha(cls, linha):
        nome, preco = linha.strip().split(";")
        return cls(nome, float(preco))

caminho = Path(__file__).parent / "lanches.txt"

with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.write("pastel;8.5\n")
    arquivo.write("\n")
    arquivo.write("coxinha;7\n")
    arquivo.write("suco;6.25\n")
    arquivo.write("   \n")

produtos = []
with open(caminho, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if not linha.strip():
            continue
        produtos.append(Produto.de_linha(linha))

total = 0
for p in produtos:
    total = total + p.preco

print(len(produtos), total)    # 3 21.75
print(f"chave: {len(produtos)}-{total}-{produtos[1].nome}")