preco = 10
quantidade = 3
total = preco * quantidade

print(total)          # ?
print(total / 4)      # ?

if total >= 30:
    frete = "grátis"
else:
    frete = "pago"
print(frete)          # ?

print("chave:", f"{total}-{total / 4}-{frete}")    # ?