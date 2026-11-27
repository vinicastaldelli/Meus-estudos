import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class Veiculo(ABC):
    def __init__(self, placa, horas, id=None):
        self.id = id
        self.placa = placa
        self.horas = horas

    @abstractmethod
    def valor(self):
        pass

    def to_params(self):
        return (self.tipo, self.placa, self.horas)

    @classmethod
    def from_row(cls, linha):
        id, tipo, placa, horas = linha
        return cls(placa, horas, id)


class Carro(Veiculo):
    tipo = "carro"

    def valor(self):
        return self.horas * 5


class Moto(Veiculo):
    tipo = "moto"

    def valor(self):
        return self.horas * 3


TIPOS = {"carro": Carro, "moto": Moto}


def criar_veiculo(linha):
    return TIPOS[linha[1]].from_row(linha)


class RepositorioVeiculos:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS veiculos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    placa TEXT NOT NULL UNIQUE,
                    horas INTEGER NOT NULL
                )
            """)

    def salvar(self, veiculo):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO veiculos (tipo, placa, hora) VALUES (?, ?, ?)",
                veiculo.to_params(),
            )
            veiculo.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, tipo, placa, horas FROM veiculos ORDER BY id"
            ).fetchall()
        return [criar_veiculo(linha) for linha in linhas]


def tentar_salvar(repo, v):
    try:
        repo.salvar(v)
        return 0
    except sqlite3.Error:
        print("Placa repetida:", v.placa)
        return 1


BANCO = Path(__file__).parent / "patio.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS veiculos")    # começa do zero a cada execução
repo = RepositorioVeiculos(BANCO)

recusados = 0
for v in [Carro("ABC1D23", 2), Moto("XYZ9K87", 3), Carro("ABC1D23", 1)]:
    recusados = recusados + tentar_salvar(repo, v)

patio = repo.listar()
print(len(patio), recusados)

# ===== TESTE DO EXCEPT (não altere estas linhas) =====
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE veiculos")    # de propósito: agora o SQL vai falhar
try:
    tentar_salvar(repo, Moto("QWE4R56", 1))
    erro_sql = "escondido"
except sqlite3.OperationalError:
    erro_sql = "apareceu"
print(f"chave: {len(patio)}-{recusados}-{sum([v.valor() for v in patio])}-{erro_sql}")
