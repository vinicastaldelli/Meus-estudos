class Playlist:
    def __init__(self, nome, musicas=None):         # era musicas=[]
        if musicas is None:      # ninguém mandou lista: cria uma nova, só desta playlist
            musicas = []
        self.nome = nome
        self.musicas = musicas

    def adicionar(self, musica):
        self.musicas.append(musica)

    def tamanho(self):
        return len(self.musicas)

treino = Playlist("Treino")
estudo = Playlist("Estudo")
festa = Playlist("Festa", ["Evidências", "Anunciação"])

treino.adicionar("Eye of the Tiger")
estudo.adicionar("Clair de Lune")

print(treino.tamanho(), estudo.tamanho(), festa.tamanho())    # 1 1 2
print(f"chave: {treino.tamanho()}-{estudo.tamanho()}-{festa.tamanho()}")    # chave: 1-1-2