notas = [7, 5, 9]
notas.append(10)

print(len(notas))     # 4
print(notas[1])       # 5

soma = 0
for nota in notas:
    soma = soma + nota
print(soma)           # 31

for i in range(3):
    print(i)          # 0, 1, 2

print("chave:", f"{len(notas)}-{notas[1]}-{soma}-{i}")    # 4-5-31-2