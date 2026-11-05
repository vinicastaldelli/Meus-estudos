class Passagem:
    total_vendidas = 0

    def __init__(self, origem, destino, preco):
        self.origem = origem
        self.destino = destino
        self.preco = preco
        Passagem.total_vendidas = Passagem.total_vendidas + 1

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], partes[1], float(partes[2]))

    def com_desconto(self, porcentagem):
        return self.preco - self.preco * porcentagem / 100

    def __str__(self):
        return f"{self.origem} para {self.destino}: R$ {self.preco:.2f}"

ida = Passagem("Goiânia", "Brasília", 90.0)
volta = Passagem.de_texto("Brasília;Goiânia;80")
print(ida)                         # Goiânia para Brasília: R$ 90.00
print(volta.com_desconto(25))      # 60.0
print(Passagem.total_vendidas)     # 2
print(f"chave: {Passagem.total_vendidas}-{volta.preco}-{ida.com_desconto(50)}")    # 2-80.0-45.0