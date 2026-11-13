from pathlib import Path

class Musica:
    def __init__(self, titulo, minutos):
        self.titulo = titulo
        self.minutos = minutos

    def para_linha(self):
        return f"{self.titulo};{self.minutos}\n"

    @classmethod
    def de_linha(cls, linha):
        titulo, minutos = linha.strip().split(";")
        return cls(titulo, int(minutos))

def salvar(musicas, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for m in musicas:
            arquivo.write(m.para_linha())

def carregar(caminho):
    musicas = []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            musicas.append(Musica.de_linha(linha))
    return musicas

caminho = Path(__file__).parent / "playlist.txt"
salvar([Musica("Asa Branca", 3), Musica("Garota de Ipanema", 5), Musica("Aquarela", 4)], caminho)
lidas = carregar(caminho)

total = 0
for m in lidas:
    total = total + m.minutos

print(lidas[1].titulo, total)    # Garota de Ipanema 12
print(f"chave: {len(lidas)}-{total}-{lidas[2].titulo}")