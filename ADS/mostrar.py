nome = "Ana"
total = 30

print("Olá")                        # Olá
print("Total:", total)              # Total: 30   (a vírgula vira espaço)
print(f"{nome} pagou {total}")      # Ana pagou 30
print(f"{total / 4}")               # 7.5   (dentro das chaves pode ir uma conta)
print(f"{nome}-{total}")            # Ana-30   (o hífen é só texto)
print("chave:", f"{nome}-{total}")  # chave: Ana-30