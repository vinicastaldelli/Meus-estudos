# Aula 14 · Exercício 07 (casa, opcional): contatos com e sem telefone
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# Contato: o __init__ recebe nome, telefone e id, com telefone=None e id=None
# como padrão. Num formulário, o campo vazio chega como "": por isso, se o
# telefone vier "", guarde None no lugar (no banco, ele vira NULL).
#   from_row(linha)   @classmethod; a linha vem na ordem (id, nome, telefone).
#   to_params()       RETORNA (nome, telefone).
#   __str__           retorna, por exemplo:
#                       #2 Bruno: 62 98888-0002
#                       #1 Ana (sem telefone)        (quando o telefone é None)
#
# RepositorioContatos: o __init__ guarda o caminho e cria a tabela contatos
# (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, telefone TEXT),
# com IF NOT EXISTS. Repare: o telefone NÃO tem NOT NULL.
#   salvar(contato)   INSERT; guarda o id gerado em contato.id.
#   listar()          RETORNA a lista de Contato, em ordem de id.
#   sem_telefone()    RETORNA a lista dos contatos cujo telefone é None,
#                     usando self.listar(), um for e o teste  is None.
#
# Exemplo, num banco ex07.db ao lado deste arquivo. Salve
# Contato("Ana"), Contato("Bruno", "62 98888-0002") e Contato("Caio", "").
# Um for com print em listar() mostra:
#   #1 Ana (sem telefone)
#   #2 Bruno: 62 98888-0002
#   #3 Caio (sem telefone)
# len(repo.sem_telefone()) dá 2.
#
# Teste você mesmo: no fim do arquivo, comece com DROP TABLE IF EXISTS contatos
# (como nos exercícios de sala) e mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   None e NULL ............ aula 14, slide 32  https://poo.leoad.com.br/aulas/aula-14/#s32
#   o texto vazio .......... aula 14, slide 33  https://poo.leoad.com.br/aulas/aula-14/#s33
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex07.py.
#    (O arquivo ex07.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
