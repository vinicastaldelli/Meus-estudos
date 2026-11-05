from abc import ABC, abstractmethod

class Assinatura(ABC):
    def __init__(self, cliente):
        self.cliente = cliente

    @abstractmethod
    def mensalidade(self):
        pass

    def anual(self):
        return self.mensalidade() * 12

class Basica(Assinatura):
    def mensalidade(self):
        return 20

class Premium(Assinatura):
    def __init__(self, cliente, telas):
        super().__init__(cliente)
        self.telas = telas

    def mensalidade(self):
        return 30 + 10 * self.telas

class Familia(Assinatura):
    def __init__(self, cliente, pessoas):
        super().__init__(cliente)
        self.pessoas = pessoas

nasceram = 0

try:
    a = Assinatura("Ana")
    nasceram = nasceram + 1
    resultado = "nasceu"
except TypeError:
    resultado = "recusada"
print("Assinatura", resultado)            # Assinatura recusada

try:
    b = Basica("Bia")
    nasceram = nasceram + 1
    resultado = "nasceu"
except TypeError:
    resultado = "recusada"
print("Basica", resultado)                # Basica nasceu

try:
    p = Premium("Caio", 2)
    nasceram = nasceram + 1
    resultado = "nasceu"
except TypeError:
    resultado = "recusada"
print("Premium", resultado)               # Premium nasceu

try:
    f = Familia("Davi", 4)
    nasceram = nasceram + 1
    resultado = "nasceu"
except TypeError:
    resultado = "recusada"
print("Familia", resultado)               # Familia recusada

print(nasceram)                         # 2
print(p.anual())                        # 600
print(f"chave: {nasceram}-{b.anual()}-{p.anual()}")    # 2-240-600