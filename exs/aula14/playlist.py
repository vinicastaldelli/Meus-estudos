import sqlite3
from pathlib import Path


class Musica:
    def __init__(self, titulo, artista, segundos, id=None):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.segundos = segundos

    @classmethod
    def from_row(cls, linha):
        id, titulo, artista, segundos = linha
        return cls(titulo, artista, segundos, id)

    def to_params(self):
        return (self.titulo, self.artista, self.segundos)


caminho = Path(__file__).parent / "playlist.db"

with sqlite3.connect(caminho) as conexao:
    conexao.execute("DROP TABLE IF EXISTS musicas")
    conexao.execute("""
        CREATE TABLE musicas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            segundos INTEGER NOT NULL
        )
    """)
    sql = "INSERT INTO musicas (titulo, artista, segundos) VALUES (?, ?, ?)"
    conexao.execute(sql, Musica("Asa Branca", "Luiz Gonzaga", 190).to_params())
    conexao.execute(sql, Musica("Aquarela", "Toquinho", 255).to_params())
    linhas = conexao.execute("SELECT id, titulo, artista, segundos FROM musicas ORDER BY id").fetchall()

musicas = []
for linha in linhas:
    musicas.append(Musica.from_row(linha))

print(musicas[1].titulo, musicas[1].id)    # Aquarela 2
print(musicas[0].artista)                  # Luiz Gonzaga
print(f"chave: {musicas[1].artista}-{musicas[0].id}-{musicas[0].segundos + musicas[1].segundos}")