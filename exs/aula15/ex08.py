# Aula 15 · Exercício 08 (casa, desafio): o plano que muda de classe
#
# Comece o arquivo com:  import sqlite3,  from abc import ABC, abstractmethod
# e  from pathlib import Path
#
# As classes e a tabela:
#   Assinatura (abstrata): id, cliente; mensalidade() abstrato;
#                          to_params(); from_row(linha); __str__
#   Basico:   tipo = "basico",   mensalidade() RETORNA 30
#   Premium:  tipo = "premium",  mensalidade() RETORNA 60
#   RepositorioAssinaturas: caminho (o __init__ cria a tabela); salvar(assinatura);
#                           buscar_por_id(id); atualizar(assinatura);
#                           remover(id): bool; promover(id)
#   tabela assinaturas:  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                        tipo TEXT NOT NULL,  cliente TEXT NOT NULL
#
# O __str__ retorna, por exemplo:  #1 Ana (basico): R$ 30.00
# buscar_por_id(id)     RETORNA a assinatura da classe certa, ou None.
# atualizar(assinatura) grava o objeto por cima da linha do mesmo id:
#     "UPDATE assinaturas SET tipo = ?, cliente = ? WHERE id = ?"
# remover(id)           apaga a linha:  "DELETE FROM assinaturas WHERE id = ?"
#     RETORNA True se apagou e False se o id não existia (cursor.rowcount,
#     como no remover da aula 14).
# promover(id)          busca a assinatura; se ela for um Basico, cria um
#     Premium com o mesmo cliente e o mesmo id e chama atualizar com ele.
#
# Exemplo: salve Basico("Ana") e Basico("Bia"). Depois de promover(1),
# buscar_por_id(1) devolve um Premium:  #1 Ana (premium): R$ 60.00. Ninguém
# mudou o objeto: mudou o texto da coluna tipo, e o TIPOS fez o resto.
# remover(2) dá True, remover(2) de novo dá False e buscar_por_id(2) dá None.
#
# Comece o seu teste apagando a tabela da rodada anterior, como na sala:
#   BANCO = Path(__file__).parent / "ex08.db"
#   with sqlite3.connect(BANCO) as conexao:
#       conexao.execute("DROP TABLE IF EXISTS assinaturas")
#
# Teste você mesmo: no fim do arquivo, salve, promova, remova e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   atualizar e remover .... aula 14, slide 26  https://poo.leoad.com.br/aulas/aula-14/#s26
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   o repositório com tipo . aula 15, slide 14  https://poo.leoad.com.br/aulas/aula-15/#s14
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   o DROP no teste ........ aula 14, slide 29  https://poo.leoad.com.br/aulas/aula-14/#s29


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex08.py.
#    (O arquivo ex08.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
