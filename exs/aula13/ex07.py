# Aula 13 · Exercício 07 (casa, opcional): a calculadora com dicionário
#
# Escreva somar(a, b), subtrair(a, b), multiplicar(a, b) e dividir(a, b),
# cada uma RETORNANDO o resultado.
# OPERACOES: um dicionário que liga o símbolo à FUNÇÃO (sem parênteses):
#   "+" -> somar,  "-" -> subtrair,  "*" -> multiplicar,  "/" -> dividir
# calcular(a, operador, b):
#   se o operador não estiver em OPERACOES:
#       raise ValueError(f"Operador desconhecido: {operador}")
#   senão, pega a função no dicionário e RETORNA o resultado dela com a e b.
#   Sem if/elif para escolher a conta: quem escolhe é o dicionário.
#
# Exemplos:
#   calcular(8, "+", 2) retorna 10      calcular(9, "/", 2) retorna 4.5
#   Para a lista  contas = [[8, "+", 2], [9, "/", 2], [7, "-", 10]],
#   um for imprime:   8 + 2 = 10    9 / 2 = 4.5    7 - 10 = -3   (uma por linha)
#   calcular(5, "%", 2) dentro de try/except ValueError mostra:
#   Operador desconhecido: %
#
# Teste você mesmo: no fim do arquivo, chame calcular e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   função em dicionário ... aula 13, slide 7  https://poo.leoad.com.br/aulas/aula-13/#s7
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   except ... as erro ..... aula 04, slide 15  https://poo.leoad.com.br/aulas/aula-04/#s15


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
