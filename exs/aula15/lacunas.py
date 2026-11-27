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
    tipo = linha[1]
    if tipo not in TIPOS:
        raise ValueError(f"tipo desconhecido: {tipo}")
    return TIPOS[tipo].from_row(linha)


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
                "INSERT INTO veiculos (tipo, placa, horas) VALUES (?, ?, ?)",
                veiculo.to_params(),
            )
            veiculo.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, tipo, placa, horas FROM veiculos ORDER BY id"
            ).fetchall()
        return [criar_veiculo(linha) for linha in linhas]


BANCO = Path(__file__).parent / "lacunas.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS veiculos")    # começa do zero a cada execução

repo = RepositorioVeiculos(BANCO)
repo.salvar(Moto("XYZ9K87", 2))
repo.salvar(Carro("ABC1D23", 3))
repo.salvar(Moto("QWE4R56", 5))

patio = RepositorioVeiculos(BANCO).listar()
print(patio[0].tipo, patio[0].valor())    # moto 6
print(patio[1].tipo, patio[1].valor())    # carro 15
print(f"chave: {patio[2].id}-{patio[2].tipo}-{sum([v.valor() for v in patio])}")
