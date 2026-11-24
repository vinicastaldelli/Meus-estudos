import sqlite3
from pathlib import Path


class Tarefa:
    def __init__(self, descricao, prioridade, id=None):
        self.id = id
        self.descricao = descricao
        self.prioridade = prioridade

    @classmethod
    def from_row(cls, linha):
        id, descricao, prioridade = linha
        return cls(descricao, prioridade, id)

    def to_params(self):
        return (self.descricao, self.prioridade)


class RepositorioTarefas:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    prioridade INTEGER NOT NULL
                )
            """)

    def salvar(self, tarefa):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO tarefas (descricao, prioridade) VALUES (?, ?)",
                tarefa.to_params(),
            )
            tarefa.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, descricao, prioridade FROM tarefas ORDER BY id"
            ).fetchall()
        tarefas = []
        for linha in linhas:
            tarefas.append(Tarefa.from_row(linha))
        return tarefas


caminho = Path(__file__).parent / "tarefas.db"
with sqlite3.connect(caminho) as conexao:
    conexao.execute("DROP TABLE IF EXISTS tarefas")

repo = RepositorioTarefas(caminho)
repo.salvar(Tarefa("estudar", 1))
repo.salvar(Tarefa("lavar", 3))

tarefas = repo.listar()
print(tarefas[0].descricao, tarefas[0].prioridade)    # estudar 1
print(f"chave: {tarefas[1].descricao}-{tarefas[1].prioridade}-{tarefas[1].id}")