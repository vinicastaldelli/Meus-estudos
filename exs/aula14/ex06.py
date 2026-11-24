# Aula 14 · Exercício 06 (casa, opcional): a agenda cultural
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# Evento: o __init__ recebe nome, cidade, preco e id (id=None como padrão),
# com from_row (a linha vem na ordem id, nome, cidade, preco), to_params e
#   __repr__   por exemplo:  Evento('Peça infantil', 'Goiânia', 20.0, 4)
#
# RepositorioEventos: o __init__ guarda o caminho e cria a tabela eventos
# (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL,
# cidade TEXT NOT NULL, preco REAL NOT NULL), com IF NOT EXISTS.
#   salvar(evento)       INSERT; guarda o id gerado em evento.id.
#   da_cidade(cidade)    RETORNA a lista dos eventos daquela cidade, do mais
#                        barato ao mais caro:  WHERE cidade = ? ORDER BY preco
#   ate(preco_maximo)    RETORNA a lista dos eventos que custam até esse valor,
#                        em ordem de id:  WHERE preco <= ? ORDER BY id
#
# Exemplo, num banco ex06.db ao lado deste arquivo. Salve, nesta ordem:
#   Evento("Show de viola", "Goiânia", 60)
#   Evento("Feira do livro", "Anápolis", 0)
#   Evento("Festival de jazz", "Goiânia", 45)
#   Evento("Peça infantil", "Goiânia", 20)
#   Evento("Cinema na praça", "Anápolis", 10)
# da_cidade("Goiânia") mostra:
#   [Evento('Peça infantil', 'Goiânia', 20.0, 4), Evento('Festival de jazz', 'Goiânia', 45.0, 3), Evento('Show de viola', 'Goiânia', 60.0, 1)]
# ate(20) mostra os eventos de ids 2, 4 e 5.
# da_cidade("Brasília") mostra [] (lista vazia).
# Para pensar: e da_cidade("goiânia"), com g minúsculo? Rode e veja.
#
# Teste você mesmo: no fim do arquivo, comece com DROP TABLE IF EXISTS eventos
# (como nos exercícios de sala) e mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   WHERE e fetchone ....... aula 14, slide 11  https://poo.leoad.com.br/aulas/aula-14/#s11
#   SELECT e fetchall ...... aula 14, slide 10  https://poo.leoad.com.br/aulas/aula-14/#s10
#   __init__ e salvar ...... aula 14, slide 24  https://poo.leoad.com.br/aulas/aula-14/#s24
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex06.py.
#    (O arquivo ex06.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
