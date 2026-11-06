def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

calc = dobro
print(calc(5))            # 10

calc = triplo
print(calc(5))            # 15

g = calc
print(g(2) + calc(1))     # 9
print(g == triplo)        # True

h = g(4)
print(h + 1)              # 13

print(f"chave: {dobro(5)}-{calc(5)}-{g(2) + calc(1)}-{g == triplo}-{h + 1}") # 10-15-9-True-13