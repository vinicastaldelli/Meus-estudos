# Aula 15 · Exercício 05 (casa, OBRIGATÓRIO): o código de produto que não repete
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# As classes e a tabela:
#   Produto: id, codigo, nome, preco; to_params(); from_row(linha); __str__
#            o __str__ retorna, por exemplo:  #1 CAN01 Caneta: R$ 2.50
#   RepositorioProdutos: caminho (o __init__ cria a tabela); cadastrar(produto): bool;
#                        buscar_por_codigo(codigo): Produto; listar(): list
#   tabela produtos:  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     codigo TEXT NOT NULL UNIQUE,  nome TEXT NOT NULL,
#                     preco REAL NOT NULL
#
# cadastrar(produto)   tenta o INSERT. Deu certo: guarda o id gerado e RETORNA
#                      True. O banco recusou o dado (sqlite3.IntegrityError):
#                      RETORNA False. Só esse erro: erro de SQL tem que aparecer.
# buscar_por_codigo(codigo)   RETORNA o Produto, ou None se não existir.
#
# Exemplo: cadastrar ("CAN01", "Caneta", 2.5) dá True; ("CAD02", "Caderno", 25)
# dá True; ("CAN01", "Canetão", 4) dá False (código repetido);
# ("BOR03", None, 1.5) dá False (sem nome). buscar_por_codigo("CAD02") mostra
# #2 CAD02 Caderno: R$ 25.00, buscar_por_codigo("XYZ99") dá None e listar()
# tem 2 produtos.
#
# Comece o seu teste apagando a tabela da rodada anterior, como na sala:
#   BANCO = Path(__file__).parent / "ex05.db"
#   with sqlite3.connect(BANCO) as conexao:
#       conexao.execute("DROP TABLE IF EXISTS produtos")
#
# Teste você mesmo: no fim do arquivo, cadastre, busque e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   tratar o IntegrityError . aula 15, slide 22  https://poo.leoad.com.br/aulas/aula-15/#s22
#   o except largo ......... aula 15, slide 25  https://poo.leoad.com.br/aulas/aula-15/#s25
#   __init__ e salvar ...... aula 14, slide 24  https://poo.leoad.com.br/aulas/aula-14/#s24
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29

import sqlite3
from pathlib import Path

class Produto:
    def __init__(self, codigo, nome, preco, id=None):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def to_params(self):
        return (self.codigo, self.nome, self.preco)

    @classmethod
    def from_row(cls, linha):
        id, codigo, nome, preco = linha
        return cls(codigo, nome, preco, id)

    def __str__(self):
        return f"#{self.id} {self.codigo} {self.nome}: R$ {self.preco:.2f}"

class RepositorioProdutos:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT NOT NULL UNIQUE,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL
                )
            """)

    def cadastrar(self, produto):
        try:
            with sqlite3.connect(self.caminho) as conexao:
                cursor = conexao.execute(
                    "INSERT INTO produtos (codigo, nome, preco) VALUES (?, ?, ?)",
                    produto.to_params()
                )
                produto.id = cursor.lastrowid
                return True
        except sqlite3.IntegrityError:
            return False

    def buscar_por_codigo(self, codigo):
        with sqlite3.connect(self.caminho) as conexao:
            linha = conexao.execute(
                "SELECT id, codigo, nome, preco FROM produtos WHERE codigo = ?",
                (codigo,)
            ).fetchone()
        return Produto.from_row(linha) if linha else None

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, codigo, nome, preco FROM produtos ORDER BY id"
            ).fetchall()
        return [Produto.from_row(linha) for linha in linhas]


BANCO = Path(__file__).parent / "ex05.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS produtos")

repo = RepositorioProdutos(BANCO)

print(repo.cadastrar(Produto("CAN01", "Caneta", 2.5)))
print(repo.cadastrar(Produto("CAD02", "Caderno", 25)))
print(repo.cadastrar(Produto("CAN01", "Canetão", 4)))
print(repo.cadastrar(Produto("BOR03", None, 1.5)))

produto = repo.buscar_por_codigo("CAD02")
print(produto)
produto_inexistente = repo.buscar_por_codigo("XYZ99")
print(produto_inexistente)

produtos = repo.listar()
for p in produtos:
    print(p)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex05.py.
#    (O arquivo ex05.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# True
# True
# False
# False
# #2 CAD02 Caderno: R$ 25.00
# None
# #1 CAN01 Caneta: R$ 2.50
# #2 CAD02 Caderno: R$ 25.00