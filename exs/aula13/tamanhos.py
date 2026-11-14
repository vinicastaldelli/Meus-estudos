def preco_p(base):
    return base

def preco_m(base):
    return base + 10

def preco_g(base):
    return base * 2

# 1. Crie aqui o dicionário TAMANHOS: "P", "M" e "G" ligados às funções (sem parênteses)
TAMANHOS = {"P": preco_p, "M": preco_m, "G": preco_g}

def preco(tamanho, base):
    return TAMANHOS[tamanho](base)   # 2. troque esta linha: pegue a função no dicionário e chame com a base

pedido = ["G", "M", "P", "M"]
total = 0
for tamanho in pedido:
    total = total + preco(tamanho, 30)

print(preco("G", 30))
print(total)
print(f"chave: {preco('M', 25)}-{total}-{len(TAMANHOS)}")