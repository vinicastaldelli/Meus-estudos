# Aula 15 · Exercício 04 (casa, OBRIGATÓRIO): os pagamentos no banco
#
# Comece o arquivo com:  import sqlite3,  from abc import ABC, abstractmethod
# e  from pathlib import Path
#
# As classes e a tabela:
#   Pagamento (abstrata): id, valor; taxa() abstrato; to_params(); from_row(linha)
#   Pix (herda de Pagamento):     tipo = "pix",     taxa() RETORNA 0
#   Cartao (herda de Pagamento):  tipo = "cartao",  taxa() RETORNA 3% do valor
#   RepositorioPagamentos: caminho (o __init__ cria a tabela); salvar(pagamento);
#                          listar(); total_taxas()
#   tabela pagamentos:  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                       tipo TEXT NOT NULL,  valor REAL NOT NULL
#
# Use o molde da aula: tipo como atributo de classe em cada filha, to_params()
# com self.tipo, o dicionário TIPOS e a função criar_pagamento(linha), que pega
# a classe certa no TIPOS e chama o from_row DELA (tipo desconhecido:
# raise ValueError). salvar guarda o id gerado. total_taxas() RETORNA a soma
# das taxas de todos os pagamentos salvos (use self.listar()).
#
# Exemplo: salve Pix(100), Cartao(200) e Cartao(50). Depois, num repositório
# novo no mesmo arquivo de banco: listar() devolve 3 pagamentos, o segundo é
# um Cartao (confira com isinstance) e total_taxas() dá 7.5.
#
# Comece o seu teste apagando a tabela da rodada anterior, como na sala:
#   BANCO = Path(__file__).parent / "ex04.db"
#   with sqlite3.connect(BANCO) as conexao:
#       conexao.execute("DROP TABLE IF EXISTS pagamentos")
#
# Teste você mesmo: no fim do arquivo, salve, liste e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   o tipo em cada filha ... aula 15, slide 8  https://poo.leoad.com.br/aulas/aula-15/#s8
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   o repositório com tipo . aula 15, slide 14  https://poo.leoad.com.br/aulas/aula-15/#s14
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   sum .................... aula 10, slide 28  https://poo.leoad.com.br/aulas/aula-10/#s28
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29

import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path

class Pagamento(ABC):
    def __init__(self, valor, id=None):
        self.id = id
        self.valor = valor

    @abstractmethod
    def taxa(self):
        pass

    def to_params(self):
        return (self.tipo, self.valor)

    @classmethod
    def from_row(cls, linha):
        id, tipo, valor = linha
        return cls(valor, id)

class Pix(Pagamento):
    tipo = "pix"

    def taxa(self):
        return 0

class Cartao(Pagamento):
    tipo = "cartao"

    def taxa(self):
        return self.valor * 0.03

TIPOS = {"pix": Pix, "cartao": Cartao}

def criar_pagamento(linha):
    tipo = linha[1]
    if tipo not in TIPOS:
        raise ValueError(f"tipo desconhecido: {tipo}")
    return TIPOS[tipo].from_row(linha)

class RepositorioPagamentos:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS pagamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    valor REAL NOT NULL
                )
            """)

    def salvar(self, pagamento):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO pagamentos (tipo, valor) VALUES (?, ?)",
                pagamento.to_params()
            )
            pagamento.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, tipo, valor FROM pagamentos ORDER BY id"
            ).fetchall()
        return [criar_pagamento(linha) for linha in linhas]

    def total_taxas(self):
        return sum(pagamento.taxa() for pagamento in self.listar())

BANCO = Path(__file__).parent / "ex04.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS pagamentos")

repo = RepositorioPagamentos(BANCO)
repo.salvar(Pix(100))
repo.salvar(Cartao(200))
repo.salvar(Cartao(50))

pagamentos = repo.listar()
print(pagamentos)

print(isinstance(pagamentos[1], Cartao))

print(repo.total_taxas())

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex04.py.
#    (O arquivo ex04.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# [<__main__.Pix object at 0x000002969E574B90>, <__main__.Cartao object at 0x000002969E574CD0>, <__main__.Cartao object at 0x000002969E4D3100>]
# True
# 7.5