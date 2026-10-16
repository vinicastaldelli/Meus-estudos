class Cofre:
    def __init__(self, dono, valor):
        self.dono = dono
        self.__valor = valor

    def ver_valor(self):
        return self.__valor

c = Cofre("Ana", 100)
c.__valor = 99

print(c.__valor)           # 99
print(c.ver_valor())       # 100
print(c._Cofre__valor)     # 100
print(f"chave: {c.__valor}-{c.ver_valor()}-{c._Cofre__valor}")   # ?