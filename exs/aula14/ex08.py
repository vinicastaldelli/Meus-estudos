# Aula 14 · Exercício 08 (casa, desafio): o repositório de alunos, agora no banco
#
# Comece o arquivo com:  import sqlite3  e  from pathlib import Path
#
# Lembra do RepositorioAlunos da aula 10, que guardava os alunos num dicionário
# com a matrícula como chave? Escreva a mesma classe, com os mesmos métodos e
# mais um listar(), guardando os alunos num banco SQLite.
#
# Aluno: o __init__ recebe matricula, nome e media, com from_row (a linha vem
# na ordem matricula, nome, media), to_params e
#   __repr__   por exemplo:  Aluno('2026002', 'Bruno', 6.0)
#
# RepositorioAlunos: o __init__ recebe o caminho, guarda e cria a tabela alunos:
#   matricula TEXT PRIMARY KEY, nome TEXT NOT NULL, media REAL NOT NULL
#   A chave primária agora é a matrícula, um texto: sem AUTOINCREMENT e sem
#   lastrowid (quem escolhe a matrícula é você).
#   adicionar(aluno)    INSERT do aluno.
#   listar()            RETORNA a lista de Aluno, em ordem de matrícula.
#   buscar(matricula)   RETORNA o Aluno, ou None se a matrícula não existir.
#   remover(matricula)  RETORNA True se apagou, False se não existia.
#   quantidade()        RETORNA quantos alunos estão guardados (use self.listar()).
#   melhor()            RETORNA o ALUNO com a maior média: max com key, sobre listar().
#
# Exemplo, o mesmo da aula 10, num banco ex08.db ao lado deste arquivo:
#   adicione Aluno("2026001", "Ana", 8.5), Aluno("2026002", "Bruno", 6.0)
#   e Aluno("2026003", "Caio", 9.2)
#   quantidade() dá 3, buscar("2026002") mostra Aluno('2026002', 'Bruno', 6.0),
#   buscar("2026999") mostra None e melhor().nome dá Caio.
#   remover("2026003") dá True; de novo, False; e melhor().nome passa a ser Ana.
# Para pensar 1: na aula 10, um RepositorioAlunos() novo nascia vazio. E agora,
#   um RepositorioAlunos novo com o mesmo ex08.db? Rode e explique num comentário.
# Para pensar 2: adicionar duas vezes a mesma matrícula dá
#   sqlite3.IntegrityError: UNIQUE constraint failed: alunos.matricula
#   Por quê? (Tratar esse erro é assunto da próxima aula.)
#
# Teste você mesmo: no fim do arquivo, comece com DROP TABLE IF EXISTS alunos
# (como nos exercícios de sala) e mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   atualizar e remover .... aula 14, slide 26  https://poo.leoad.com.br/aulas/aula-14/#s26
#   from_row e to_params ... aula 14, slide 18  https://poo.leoad.com.br/aulas/aula-14/#s18


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex08.py.
#    (O arquivo ex08.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
