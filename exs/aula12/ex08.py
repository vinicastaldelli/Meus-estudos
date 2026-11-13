# Aula 12 · Exercício 08 (casa, desafio): o repositório que lembra
#
# Comece o arquivo com:  import json  e  from pathlib import Path
#
# Contato: nome e telefone, com para_dict() e de_dict(dados), como no ex03.
#
# RepositorioContatos: guarda os contatos num dicionário (a chave é o nome)
#   e grava tudo num arquivo JSON a cada mudança.
#   __init__(caminho)   guarda o caminho, cria o dicionário vazio e CARREGA o
#                       arquivo, se ele existir (FileNotFoundError: começa vazio).
#   salvar()            grava a lista de dicionários (um por contato) com json.dump.
#   adicionar(contato)  guarda no dicionário e chama o salvar().
#   buscar(nome)        RETORNA o contato, ou None se não existir. Use .get().
#   remover(nome)       se existir, apaga, chama o salvar() e RETORNA True;
#                       se não existir, RETORNA False.
#   quantidade()        RETORNA quantos contatos há.
#
# Exemplo: na 1ª vez que rodar, adicione Contato("Ana", "62 99999-0001") e
# Contato("Bruno", "62 98888-0002"): quantidade() dá 2. Rode de novo SEM
# adicionar ninguém: o repositório já começa com 2, porque leu o arquivo.
# Remova o Bruno e rode mais uma vez: 1 contato. buscar("Ana").telefone dá
# 62 99999-0001, e buscar("Zé") dá None.
#
# Teste você mesmo: no fim do arquivo, crie o repositório, mexa nele e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   dicionário no __init__ . aula 10, slide 42  https://poo.leoad.com.br/aulas/aula-10/#s42
#   [ ] × .get() ........... aula 10, slide 34  https://poo.leoad.com.br/aulas/aula-10/#s34
#   para_dict e de_dict .... aula 12, slide 23  https://poo.leoad.com.br/aulas/aula-12/#s23
#   salvar a lista ......... aula 12, slide 26  https://poo.leoad.com.br/aulas/aula-12/#s26
#   carregar a lista ....... aula 12, slide 28  https://poo.leoad.com.br/aulas/aula-12/#s28
#   FileNotFoundError ...... aula 11, slide 17  https://poo.leoad.com.br/aulas/aula-11/#s17


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
