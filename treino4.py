# 1ª VA · Treino 4: as corridas do aplicativo
#
# O import do abc já está no arquivo. Escreva:
#
# 1. Corrida, uma classe ABSTRATA (herda de ABC):
#    - o __init__ recebe passageiro e km. Guarda o passageiro e
#      grava km com self.km = km, para passar pelo setter;
#    - km é uma property com setter que recusa zero ou negativo:
#          raise ValueError("distância inválida")
#    - preco() e categoria() são métodos ABSTRATOS;
#    - __str__ RETORNA, por exemplo:   Moto: Bia, 8 km, R$ 15.00
#    - __lt__ compara duas corridas pelo preco(). Se a outra não
#      for uma Corrida, RETORNA NotImplemented.
#
# 2. Duas filhas, cada uma com preco() e categoria():
#    Comum   categoria "Comum", preço: 5 reais + 2 reais por km
#    Moto    categoria "Moto",  preço: 3 reais + 1,50 por km
# Nenhum print dentro das classes.


from abc import ABC, abstractmethod

class Corrida(ABC):
    def __init__(self, passageiro, km):
        self.passageiro = passageiro
        self.km = km

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, valor):
        if valor <= 0:
            raise ValueError("distância inválida")
        self._km = valor

    @abstractmethod
    def preco(self):
        pass

    @abstractmethod
    def categoria(self):
        pass

    def __str__(self):
        return f"{self.categoria}: {self.passageiro}, {self.km} km, R$ {self.preco():.2f}"
    
    def __str__(self):                  # concreto que usa os abstratos
        inicio = f"{self.categoria()}: {self.passageiro}"
        return f"{inicio}, {self.km} km, R$ {self.preco():.2f}"

    def __lt__(self, outra):
        if isinstance(outra, Corrida):
            return self.preco() < outra.preco()
        return NotImplemented


class Comum(Corrida):
    def preco(self):
        return 5 + self.km * 2

    def categoria(self):
        return "Comum"

class Moto(Corrida):
    def preco(self):
        return 3 + self.km * 1.5

    def categoria(self):
        return "Moto"

# ===== TESTE (não altere estas linhas) =====
ana = Comum("Ana", 8)
bia = Moto("Bia", 8)
caio = Comum("Caio", 2.5)

print(ana)                    # Comum: Ana, 8 km, R$ 21.00
print(bia)                    # Moto: Bia, 8 km, R$ 15.00
print(caio)                   # Comum: Caio, 2.5 km, R$ 10.00
print(bia < ana)              # True
print(ana < caio)             # False

total = 0
for corrida in [ana, bia, caio]:
    total = total + corrida.preco()
print(f"Total do dia: R$ {total:.2f}")    # Total do dia: R$ 46.00

try:
    ana.km = 0
except ValueError as erro:
    print("recusado:", erro)  # recusado: distância inválida
print(ana.km)                 # 8

try:
    Corrida("Duda", 5)
    generica = "nasceu"
except TypeError:
    generica = "recusada"
print("Corrida genérica:", generica)    # Corrida genérica: recusada

try:
    resultado = ana < 10
    comparou = "sim"
except TypeError:
    comparou = "não"
print("comparou com número?", comparou)    # comparou com número? não