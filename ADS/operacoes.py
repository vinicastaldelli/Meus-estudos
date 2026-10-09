print(7 / 2)      # 3.5   (a divisão / sempre dá float)
print(7 // 2)     # 3     (divisão inteira)
print(7 % 2)      # 1     (resto da divisão)
print(2 ** 3)     # 8     (potência)

print("20" + "1")       # 201   (+ em texto junta)
print(int("20") + 1)    # 21    (int() converte texto em número)

idade = input("Sua idade: ")    # o usuário digita 20
print(type(idade))              # <class 'str'>   (input sempre devolve texto)
idade = int(idade)
print(idade + 1)                # 21