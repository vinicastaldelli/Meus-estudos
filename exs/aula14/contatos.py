import sqlite3
from pathlib import Path

caminho = Path(__file__).parent / "contatos.db"

with sqlite3.connect(caminho) as conexao:
    conexao.execute("DROP TABLE IF EXISTS contatos")
    conexao.execute("""
        CREATE TABLE contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT
        )
    """)
    sql = "INSERT INTO contatos (nome, telefone) VALUES (?, ?)"
    conexao.execute(sql, ("Ana", None))
    conexao.execute(sql, ("", "62 99999-0001"))
    conexao.execute(sql, ("Caio", ""))
    conexao.execute(sql, ("Duda", None))
    conexao.execute(sql, ("Eva", ""))
    conexao.execute(sql, ("Fábio", None))
    linhas = conexao.execute("SELECT id, nome, telefone FROM contatos ORDER BY id").fetchall()

sem_telefone = 0      # quem tem telefone None (NULL no banco)
telefone_vazio = 0    # quem tem telefone "" (texto vazio)
for id, nome, telefone in linhas:
    if telefone is None:
        sem_telefone = sem_telefone + 1
    if telefone == "":
        telefone_vazio = telefone_vazio + 1

print(len(linhas))              # 6
print(linhas[0])                # (1, 'Ana', None)
print(linhas[1][1] == "")       # True
print(sem_telefone)             # 3
print(telefone_vazio)           # 2
print(f"chave: {len(linhas)}-{linhas[3][2]}-{sem_telefone}-{telefone_vazio}")