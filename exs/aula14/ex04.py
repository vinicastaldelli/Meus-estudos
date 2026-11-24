# Aula 14 · Exercício 04 (casa, OBRIGATÓRIO): a estante de livros no banco
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# Livro: o __init__ recebe titulo, autor, paginas e id (id=None como padrão)
# e guarda os quatro com self.
#   from_row(linha)  construtor alternativo (@classmethod). A linha vem na ordem
#                    (id, titulo, autor, paginas). RETORNA cls(...).
#   to_params()      RETORNA (titulo, autor, paginas).
#   __repr__         retorna, por exemplo:
#                    Livro('Vidas Secas', 'Graciliano Ramos', 176, 1)
#
# RepositorioLivros: o __init__ recebe o caminho do banco, guarda em self.caminho
# e cria a tabela livros, com IF NOT EXISTS e estas colunas:
#   id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL,
#   autor TEXT NOT NULL, paginas INTEGER NOT NULL
#   salvar(livro)   INSERT com ? e livro.to_params(); guarda em livro.id o id
#                   que o banco gerou (cursor.lastrowid).
#   listar()        RETORNA a lista de objetos Livro, em ordem de id.
#   buscar(id)      RETORNA o Livro com esse id, ou None se não existir.
# Cada método abre o banco com:  with sqlite3.connect(self.caminho) as conexao:
#
# Exemplo, num banco ex04.db ao lado deste arquivo
# (BANCO = Path(__file__).parent / "ex04.db"). Salve:
#   Livro("Vidas Secas", "Graciliano Ramos", 176)
#   Livro("Dom Casmurro", "Machado de Assis", 256)
#   Livro("A Hora da Estrela", "Clarice Lispector", 88)
# listar() mostra os 3, com ids 1, 2 e 3. buscar(2) mostra o Dom Casmurro.
# buscar(10) mostra None. A soma das páginas dos livros de listar() dá 520.
#
# Teste você mesmo: no fim do arquivo, comece apagando a tabela, como nos
# exercícios de sala, para a saída ser a mesma toda vez que rodar:
#     with sqlite3.connect(BANCO) as conexao:
#         conexao.execute("DROP TABLE IF EXISTS livros")
# Depois crie o repositório, salve, liste, busque e mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   from_row e to_params ... aula 14, slide 18  https://poo.leoad.com.br/aulas/aula-14/#s18
#   __init__ e salvar ...... aula 14, slide 24  https://poo.leoad.com.br/aulas/aula-14/#s24
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

import sqlite3
from pathlib import Path

class Livro:
    def __init__(self, titulo, autor, paginas, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    @classmethod
    def from_row(cls, linha):
        id, titulo, autor, paginas = linha
        return cls(titulo, autor, paginas, id)

    def to_params(self):
        return (self.titulo, self.autor, self.paginas)

    def __repr__(self):
        return f"Livro('{self.titulo}', '{self.autor}', {self.paginas}, {self.id})"


class RepositorioLivros:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    paginas INTEGER NOT NULL
                )
            """)

    def salvar(self, livro):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO livros (titulo, autor, paginas) VALUES (?, ?, ?)",
                livro.to_params(),
            )
            livro.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, titulo, autor, paginas FROM livros ORDER BY id"
            ).fetchall()
        return [Livro.from_row(linha) for linha in linhas]

    def buscar(self, id):
        with sqlite3.connect(self.caminho) as conexao:
            linha = conexao.execute(
                "SELECT id, titulo, autor, paginas FROM livros WHERE id = ?",
                (id,),
            ).fetchone()
        if linha is None:
            return None
        return Livro.from_row(linha)

BANCO = Path(__file__).parent / "ex04.db"

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS livros")

repo = RepositorioLivros(BANCO)
repo.salvar(Livro("Vidas Secas", "Graciliano Ramos", 176))
repo.salvar(Livro("Dom Casmurro", "Machado de Assis", 256))
repo.salvar(Livro("A Hora da Estrela", "Clarice Lispector", 88))

livros = repo.listar()
print(livros)
print(repo.buscar(2))
print(repo.buscar(10))
print(sum(livro.paginas for livro in livros))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex04.py.
#    (O arquivo ex04.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# [Livro('Vidas Secas', 'Graciliano Ramos', 176, 1), Livro('Dom Casmurro', 'Machado de Assis', 256, 2), Livro('A Hora da Estrela', 'Clarice Lispector', 88, 3)]
# Livro('Dom Casmurro', 'Machado de Assis', 256, 2)
# None
# 520