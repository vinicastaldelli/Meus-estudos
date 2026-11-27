import sqlite3
from pathlib import Path

BANCO = Path(__file__).parent / "culpado.db"

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS veiculos")    # começa do zero a cada execução
    conexao.execute("""
        CREATE TABLE veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            placa TEXT NOT NULL UNIQUE,
            horas INTEGER NOT NULL
        )
    """)


def tentar(sql, valores):
    try:
        with sqlite3.connect(BANCO) as conexao:
            conexao.execute(sql, valores)
        return "ok"
    except sqlite3.IntegrityError:
        return "dado"
    except sqlite3.Error:
        return "sql"

INSERIR = "INSERT INTO veiculos (tipo, placa, horas) VALUES (?, ?, ?)"

r1 = tentar(INSERIR, ("carro", "ABC1D23", 2))
r2 = tentar(INSERIR, ("moto", "ABC1D23", 1))
r3 = tentar("INSERT INTO veiculo (tipo, placa, horas) VALUES (?, ?, ?)", ("moto", "XYZ9K87", 1))
r4 = tentar(INSERIR, ("moto", "XYZ9K87", None))
r5 = tentar(INSERIR, ("moto", "", 1))
r6 = tentar("SELECT id, tipo, placas FROM veiculos", ())

print(r1, r2, r3)    # ok dado sql
print(r4, r5, r6)    # dado ok sql
print(f"chave: {r1}-{r2}-{r3}-{r4}-{r5}-{r6}")