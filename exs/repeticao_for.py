frutas = ["banana", "maçã", "uva"]

for fruta in frutas:
    print("Eu gosto de", fruta)
# Eu gosto de banana
# Eu gosto de maçã
# Eu gosto de uva

for i in range(3):
    print(i)
# 0
# 1
# 2

for i in range(1, 4):
    print(i, "x 5 =", i * 5)
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15

precos = [12, 5, 30]
soma = 0
for preco in precos:
    soma = soma + preco
print("Total:", soma)    # Total: 47