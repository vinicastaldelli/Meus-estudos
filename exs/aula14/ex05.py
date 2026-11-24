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


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex05.py.
#    (O arquivo ex05.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
