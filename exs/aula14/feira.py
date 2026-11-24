import sqlite3
from pathlib import Path

caminho = Path(__file__).parent / "feira.db"

conexao = sqlite3.connect(caminho)
conexao.execute("DROP TABLE IF EXISTS frutas")
conexao.execute("""
    CREATE TABLE frutas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
""")
conexao.execute("INSERT INTO frutas (nome, preco) VALUES (?, ?)", ("banana", 6))
conexao.execute("INSERT INTO frutas (nome, preco) VALUES (?, ?)", ("maçã", 9.5))
conexao.execute("INSERT INTO frutas (nome, preco) VALUES (?, ?)", ("uva", 9))
conexao.commit()

linhas = conexao.execute("SELECT id, nome, preco FROM frutas ORDER BY id").fetchall()       # todas as frutas: id, nome e preco, em ordem de id
caras = conexao.execute("SELECT nome FROM frutas WHERE preco > ?", (2,)).fetchall()    # só o nome das frutas com preço MAIOR que 9
segunda = conexao.execute("SELECT nome, preco FROM frutas WHERE id = ?", (2,)).fetchone()   # nome e preço da fruta de id 2 (uma linha só)
nada = conexao.execute("SELECT nome FROM frutas WHERE id = ?", (7,)).fetchone()   # o nome da fruta de id 7, que não existe (uma linha só)
conexao.close()

print(len(linhas))     # 3
print(linhas[0])       # (1, 'banana', 6.0)
print(len(caras))      # 1
print(segunda)         # ('maçã', 9.5)
print(nada)            # None
print(f"chave: {linhas[2][0]}-{segunda[1]}-{linhas[0][2]}-{len(caras)}-{nada}")