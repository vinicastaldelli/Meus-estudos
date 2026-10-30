class Dinheiro:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        if isinstance(outro, Dinheiro):
            return Dinheiro(self.valor + outro.valor)
        return NotImplemented

    def __eq__(self, outro):
        if isinstance(outro, Dinheiro):
            return self.valor == outro.valor
        return NotImplemented

    def __repr__(self):
        return f"Dinheiro({self.valor})"

a = Dinheiro(12.5)
b = Dinheiro(7.5)

print(a + b)                    # Dinheiro(20.0)
print(a, b)                     # Dinheiro(12.5) Dinheiro(7.5)
print(a + b == Dinheiro(20))    # True
print(a == 12.5)                # False
print(f"chave: {(a + b + a).valor}-{a + b == Dinheiro(20)}-{a == 12.5}-{a.__eq__(12.5)}")