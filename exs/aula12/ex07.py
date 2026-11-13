# Aula 12 · Exercício 07 (casa, opcional): do texto para o JSON
#
# Comece o arquivo com:  import json  e  from pathlib import Path
#
# Livro: o __init__ recebe titulo, autor e paginas e guarda os três.
#   de_linha(linha)  construtor alternativo (@classmethod): lê uma linha como
#                    Dom Casmurro;Machado de Assis;256   (paginas volta como int)
#   para_dict()      RETORNA {"titulo": ..., "autor": ..., "paginas": ...}
#
# converter(origem, destino): lê o arquivo de texto origem (pulando as linhas em
#   branco), transforma cada linha num Livro e grava a lista de dicionários no
#   arquivo JSON destino, com json.dump (ensure_ascii=False, indent=2).
#   RETORNA quantos livros foram convertidos.
#
# Exemplo: grave (com write, no próprio programa) um livros.txt ao lado deste
# arquivo com estas 3 linhas:
#   Dom Casmurro;Machado de Assis;256
#   A Hora da Estrela;Clarice Lispector;88
#   Vidas Secas;Graciliano Ramos;176
# converter(...) RETORNA 3. Abra o livros.json no VS Code e confira: as páginas
# aparecem sem aspas, porque são números.
#
# Teste você mesmo: no fim do arquivo, grave o livros.txt, converta e mostre o
# resultado com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   de_linha e para_linha .. aula 12, slide 6  https://poo.leoad.com.br/aulas/aula-12/#s6
#   linha em branco ........ aula 12, slide 12  https://poo.leoad.com.br/aulas/aula-12/#s12
#   para_dict e de_dict .... aula 12, slide 23  https://poo.leoad.com.br/aulas/aula-12/#s23
#   json.dump e json.load .. aula 12, slide 18  https://poo.leoad.com.br/aulas/aula-12/#s18
#   salvar a lista ......... aula 12, slide 26  https://poo.leoad.com.br/aulas/aula-12/#s26


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
