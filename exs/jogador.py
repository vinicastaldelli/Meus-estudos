class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            raise ValueError("vida não pode ser negativa")
        self._vida = valor

heroi = Jogador("Link", 100)
recusas = 0

for nova in [80, -5, 60, -20]:
    try:
        heroi.vida = nova
    except ValueError as erro:
        print("recusado:", erro)
        recusas = recusas + 1

print(heroi.vida)
print(f"chave: {heroi.nome}-{heroi.vida}-{recusas}")