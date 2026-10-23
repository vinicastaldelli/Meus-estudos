# Aula 05 · Exercício 07 (casa, opcional): Playlist e Musica (associação)
#
# Musica: o __init__ recebe titulo e segundos.
#   segundos  @property e @segundos.setter. O setter RECUSA 0 ou menos:
#                 raise ValueError("música precisa durar")
#   __repr__  retorna, por exemplo: Musica('Evidências', 300)
# Playlist: o __init__ recebe nome, guarda, e cria self.musicas como lista vazia.
#   adicionar(musica)  recebe uma Musica JÁ CRIADA fora da playlist (associação)
#                      e coloca na lista.
#   duracao_total()    RETORNA a soma dos segundos de todas as músicas, usando um for.
#   minutos()          RETORNA a duração total dividida por 60.
#
# Exemplos:
#   evidencias = Musica("Evidências", 300) e tempo = Musica("Tempo Perdido", 240).
#   Uma playlist com as duas: duracao_total() retorna 540 e minutos() retorna 9.0.
#
# No fim, coloque a MESMA música em duas playlists e mostre, com print, que
# é um objeto só: compare com == a música das duas listas (dá True).
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   associação ............. aula 05, slide 39  https://poo.leoad.com.br/aulas/aula-05/#s39
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
