# Aula 15 · Exercício 06 (casa, opcional): a folha de pagamento, com uma coluna a mais
#
# Comece o arquivo com:  import sqlite3,  from abc import ABC, abstractmethod
# e  from pathlib import Path
#
# As classes e a tabela:
#   Funcionario (abstrata): id, nome, base; salario() abstrato;
#                           to_params(); from_row(linha)
#   Clt:         tipo = "clt",         salario() RETORNA base
#   Estagiario:  tipo = "estagiario",  salario() RETORNA base / 2
#   Freelancer:  tipo = "freelancer",  tem também horas;
#                salario() RETORNA base * horas;
#                sobrescreve to_params() e from_row() para levar e trazer horas
#   RepositorioFuncionarios: caminho (o __init__ cria a tabela); salvar(funcionario);
#                            listar(); listar_por_tipo(tipo); folha()
#   tabela funcionarios:  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         tipo TEXT NOT NULL,  nome TEXT NOT NULL,
#                         base REAL NOT NULL,  horas INTEGER
#   (horas sem NOT NULL: quem não é freelancer grava None, que vira NULL)
#
# listar_por_tipo(tipo)   RETORNA só os daquele tipo: SELECT ... WHERE tipo = ?
# folha()                 RETORNA a soma dos salários de todos (use self.listar())
#
# Exemplo: salve Clt("Ana", 3000), Estagiario("Bia", 1600),
# Freelancer("Caio", 50, 20) e Clt("Duda", 2500). listar_por_tipo("clt")
# devolve a Ana e a Duda, o Caio volta Freelancer com horas 20, e a folha()
# dá 7300.0.
#
# Comece o seu teste apagando a tabela da rodada anterior, como na sala:
#   BANCO = Path(__file__).parent / "ex06.db"
#   with sqlite3.connect(BANCO) as conexao:
#       conexao.execute("DROP TABLE IF EXISTS funcionarios")
#
# Teste você mesmo: no fim do arquivo, salve, liste e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   filha com coluna a mais . aula 15, slide 33  https://poo.leoad.com.br/aulas/aula-15/#s33
#   a hierarquia na tabela . aula 15, slide 32  https://poo.leoad.com.br/aulas/aula-15/#s32
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   WHERE e fetchone ....... aula 14, slide 11  https://poo.leoad.com.br/aulas/aula-14/#s11
#   None e NULL ............ aula 14, slide 32  https://poo.leoad.com.br/aulas/aula-14/#s32
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex06.py.
#    (O arquivo ex06.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
