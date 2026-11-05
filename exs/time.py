class Tecnico:
    def __init__(self, nome):
        self.nome = nome

class Jogador:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class Time:
    def __init__(self, nome, tecnico):
        self.nome = nome
        self.tecnico = tecnico
        self.jogadores = []

    def contratar(self, nome, numero):
        jogador = Jogador(nome, numero)
        self.jogadores.append(jogador)

    def elenco(self):
        return len(self.jogadores)

professor = Tecnico("Rafael")
vila = Time("Vila Nova", professor)
vila.contratar("Pedro", 9)
vila.contratar("Caio", 10)

print(vila.elenco())                     # 2
print(vila.jogadores[1].nome)            # Caio
print(vila.tecnico == professor)         # True
print(f"chave: {vila.elenco()}-{vila.jogadores[0].numero}-{vila.tecnico.nome}-{vila.tecnico == professor}")