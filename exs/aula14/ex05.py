# Aula 14 · Exercício 05 (casa, OBRIGATÓRIO): as despesas da casa
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# Despesa: o __init__ recebe descricao, valor e id (id=None como padrão).
#   Antes de guardar, se a descricao for None ou só espaços
#   (descricao.strip() == ""), faça:
#       raise ValueError("a descrição não pode ficar vazia")
#   (o NOT NULL do banco recusa o None, mas deixa passar o texto vazio).
#   from_row(linha)  @classmethod; a linha vem na ordem (id, descricao, valor).
#   to_params()      RETORNA (descricao, valor).
#   __repr__         retorna, por exemplo:  Despesa('Luz', 180.5, 1)
#
# RepositorioDespesas: o __init__ recebe o caminho, guarda e cria a tabela
# despesas (IF NOT EXISTS), com as colunas:
#   id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL, valor REAL NOT NULL
#   salvar(despesa)     INSERT; guarda o id gerado em despesa.id.
#   listar()            RETORNA a lista de Despesa, em ordem de id.
#   atualizar(despesa)  UPDATE da descricao e do valor, WHERE id = ? (o id da despesa).
#   remover(id)         RETORNA True se apagou a linha, False se ela não existia.
#   total()             RETORNA a soma dos valores, usando self.listar() e um for.
#
# Exemplo, num banco ex05.db ao lado deste arquivo:
#   salve Despesa("Luz", 180.5), Despesa("Água", 95) e Despesa("Internet", 120)
#   listar() mostra: [Despesa('Luz', 180.5, 1), Despesa('Água', 95.0, 2), Despesa('Internet', 120.0, 3)]
#   total() dá 395.5
#   mude o valor da Água para 110 no objeto e chame atualizar: total() dá 410.5
#   remover(3) dá True, remover(3) de novo dá False, e total() dá 290.5
#   Despesa("   ", 50), dentro de try/except ValueError, mostra:
#   a descrição não pode ficar vazia
#
# Teste você mesmo: no fim do arquivo, comece com DROP TABLE IF EXISTS despesas
# (como nos exercícios de sala) e mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   raise .................. aula 03, slide 19  https://poo.leoad.com.br/aulas/aula-03/#s19
#   o texto vazio .......... aula 14, slide 33  https://poo.leoad.com.br/aulas/aula-14/#s33
#   atualizar e remover .... aula 14, slide 26  https://poo.leoad.com.br/aulas/aula-14/#s26
#   o repositório em uso ... aula 14, slide 28  https://poo.leoad.com.br/aulas/aula-14/#s28
#   CREATE TABLE ........... aula 14, slide 7  https://poo.leoad.com.br/aulas/aula-14/#s7

import sqlite3
from pathlib import Path

class Despesa:
    def __init__(self, descricao, valor, id=None):
        if descricao.strip() == "":
            raise ValueError("a descrição não pode ficar vazia")
        self.descricao = descricao
        self.valor = valor
        self.id = id

    @classmethod
    def from_row(cls, linha):
        id, descricao, valor = linha
        return cls(descricao, valor, id)

    def to_params(self):
        return (self.descricao, self.valor)

    def __repr__(self):
        return f"Despesa('{self.descricao}', {self.valor}, {self.id})"

class RepositorioDespesas:
    def __init__(self, caminho):
        self.caminho = Path(caminho)
        conexao = sqlite3.connect(self.caminho)
        try:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS despesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
                )
            """)
            conexao.commit()
        finally:
            conexao.close()

    def salvar(self, despesa):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO despesas (descricao, valor) VALUES (?, ?)",
                despesa.to_params(),
            )
            despesa.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, descricao, valor FROM despesas ORDER BY id"
            ).fetchall()
        return [Despesa.from_row(linha) for linha in linhas]

    def atualizar(self, despesa):
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute(
            "UPDATE despesas SET descricao = ?, valor = ? WHERE id = ?",
            despesa.to_params() + (despesa.id,),
        )

    def remover(self, id):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute("DELETE FROM despesas WHERE id = ?", (id,),)
        return cursor.rowcount > 0

    def total(self):
        soma = 0.0
        for despesa in self.listar():
            soma += despesa.valor
        return soma

caminho_banco = Path(__file__).with_name("ex05.db")

conexao = sqlite3.connect(caminho_banco)
try:
    conexao.execute("DROP TABLE IF EXISTS despesas")
    conexao.commit()
finally:
    conexao.close()

repositorio = RepositorioDespesas(caminho_banco)

luz = Despesa("Luz", 180.5)
agua = Despesa("Água", 95)
internet = Despesa("Internet", 120)

for despesa in (luz, agua, internet):
    repositorio.salvar(despesa)

print(repositorio.listar())
print(repositorio.total())

agua.valor = 110
repositorio.atualizar(agua)
print(repositorio.total())

print(repositorio.remover(3))
print(repositorio.remover(3))
print(repositorio.total())

try:
    Despesa("   ", 50)
except ValueError as erro:
    print(erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex05.py.
#    (O arquivo ex05.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# [Despesa('Luz', 180.5, 1), Despesa('Água', 95.0, 2), Despesa('Internet', 120.0, 3)]
# 395.5
# 410.5
# True
# False
# 290.5
# a descrição não pode ficar vazia