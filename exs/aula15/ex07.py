# Aula 15 · Exercício 07 (casa, opcional): as reservas da pousada
#
# Comece o arquivo com:  import sqlite3,  from abc import ABC, abstractmethod
# e  from pathlib import Path
#
# As classes e a tabela:
#   Quarto (abstrata): id, numero, noites; total() abstrato;
#                      to_params(); from_row(linha); __str__
#   Simples:  tipo = "simples",  total() RETORNA 150 * noites
#   Luxo:     tipo = "luxo",     total() RETORNA 400 * noites
#   RepositorioReservas: caminho (o __init__ cria a tabela); reservar(quarto): bool;
#                        buscar_por_numero(numero): Quarto; faturamento()
#   tabela reservas:  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     tipo TEXT NOT NULL,  numero INTEGER NOT NULL UNIQUE,
#                     noites INTEGER NOT NULL
#
# O __str__ retorna, por exemplo:  Quarto 201 (luxo): 2 noites, R$ 800.00
# reservar(quarto)   RETORNA True se entrou e False se o banco recusou o dado
#                    (sqlite3.IntegrityError: o quarto já está reservado).
# buscar_por_numero(numero)   RETORNA o quarto DA CLASSE CERTA, ou None.
# faturamento()      RETORNA a soma do total() de todas as reservas.
#
# Exemplo: reservar Simples(101, 3) dá True, Luxo(201, 2) dá True,
# Simples(101, 5) dá False (o 101 já está reservado) e Simples(102, 1) dá True.
# buscar_por_numero(201) mostra  Quarto 201 (luxo): 2 noites, R$ 800.00,
# buscar_por_numero(999) dá None e faturamento() dá 1400.
#
# Comece o seu teste apagando a tabela da rodada anterior, como na sala:
#   BANCO = Path(__file__).parent / "ex07.db"
#   with sqlite3.connect(BANCO) as conexao:
#       conexao.execute("DROP TABLE IF EXISTS reservas")
#
# Teste você mesmo: no fim do arquivo, reserve, busque e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   o tipo em cada filha ... aula 15, slide 8  https://poo.leoad.com.br/aulas/aula-15/#s8
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   tratar o IntegrityError . aula 15, slide 22  https://poo.leoad.com.br/aulas/aula-15/#s22
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex07.py.
#    (O arquivo ex07.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
