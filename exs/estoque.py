estoque = {"caneta": 10, "lápis": 4}

estoque["borracha"] = 5
estoque["caneta"] = estoque["caneta"] - 3
del estoque["lápis"]

print(len(estoque))               # 2
print(estoque["caneta"])          # 7
print(estoque.get("lápis", 0))    # 0
print("lápis" in estoque)         # False
print(sum(estoque.values()))      # 12

print(f"chave: {len(estoque)}-{estoque['caneta']}-{estoque.get('lápis', 0)}-{'lápis' in estoque}-{sum(estoque.values())}")
# chave: 2-7-0-False-12