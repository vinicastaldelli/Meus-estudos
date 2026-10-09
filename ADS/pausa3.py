def preco_final(preco, desconto=0):
    return preco - desconto

print(preco_final(50))        # 50
print(preco_final(50, 15))    # 35
print("chave:", f"{preco_final(100)}-{preco_final(100, 30)}")