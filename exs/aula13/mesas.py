def sem_gorjeta(conta):
    return 0

def gorjeta_10(conta):
    return conta * 10 / 100

def gorjeta_fixa(conta):
    return 5

class Mesa:
    def __init__(self, numero, conta, gorjeta):
        self.numero = numero
        self.conta = conta
        self.gorjeta = gorjeta

    def total(self):
        return self.conta + self.gorjeta(self.conta)

m1 = Mesa(1, 90, gorjeta_10)
m2 = Mesa(2, 50, sem_gorjeta)
m3 = Mesa(3, 40, gorjeta_fixa)

print(m1.total(), m2.total(), m3.total())
print(f"chave: {m1.total()}-{m2.total() + m3.total()}")