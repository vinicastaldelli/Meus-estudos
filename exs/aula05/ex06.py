# Aula 05 · Exercício 06 (casa, opcional): o livro e os seus capítulos
#
# Capitulo: o __init__ recebe titulo e paginas, e guarda os dois.
#   paginas  @property e @paginas.setter. O setter RECUSA 0 ou menos:
#                raise ValueError("capítulo precisa de páginas")
# Livro: o __init__ recebe titulo, guarda, e cria self.capitulos como lista vazia.
#   adicionar_capitulo(titulo, paginas)  CRIA o Capitulo ali dentro
#                                        (composição) e guarda na lista.
#   total_paginas()       RETORNA a soma das páginas de todos os capítulos,
#                         usando um for.
#   capitulo_mais_longo() RETORNA o TÍTULO do capítulo com mais páginas,
#                         usando um for. Se o livro não tiver capítulo
#                         nenhum, retorna None.
#                         Dica: comece guardando o primeiro capítulo e
#                         compare com os outros dentro do for.
#
# Exemplos:
#   Um livro com "O começo" (12 páginas), "A viagem" (30) e "O fim" (8):
#   total_paginas() retorna 50 e capitulo_mais_longo() retorna A viagem.
#   Um livro novo, sem capítulos: total_paginas() retorna 0 e
#   capitulo_mais_longo() retorna None.
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois livros e mostre
# os resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
