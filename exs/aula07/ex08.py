# Aula 07 · Exercício 08 (casa, desafio): a classe Fracao
#
# O __init__ recebe numerador e denominador e guarda a fração já SIMPLIFICADA:
# Fracao(2, 4) guarda 1 e 2. Para simplificar, divida os dois (com //) pelo mdc.
# Denominador 0 é recusado logo no começo do __init__:
#     raise ValueError("denominador não pode ser zero")
# numerador e denominador: @property SÓ DE LEITURA (guarde em self._numerador
# e self._denominador): a fração não muda depois de criada.
# de_texto  @classmethod: recebe "3/4" e RETORNA Fracao(3, 4) (use split("/")
#           e int()). Fracao.de_texto("2/4") dá 1/2.
# Escreva a função mdc(a, b) fora da classe, com while:
#   enquanto b for diferente de 0:  resto = a % b,  depois a = b,  depois b = resto.
#   No fim, o mdc é o a.  Exemplo: mdc(2, 4) dá 2, mdc(6, 9) dá 3.
# __add__   Fracao(1, 2) + Fracao(1, 3) dá 5/6
#           (numerador: a*d + c*b;  denominador: b*d, para a/b + c/d)
# __mul__   Fracao(2, 3) * Fracao(3, 4) dá 1/2
# __eq__    Fracao(1, 2) == Fracao(3, 6) dá True, e Fracao(1, 2) == 0.5 dá False
# __lt__    Fracao(1, 3) < Fracao(1, 2) dá True   (a/b < c/d quando a*d < c*b)
# __str__   retorna, por exemplo:  1/2
# __repr__  retorna, por exemplo:  Fracao(1, 2)
# Os operadores RETORNAM uma Fracao NOVA (ou True/False) e não mudam o self.
# Se o outro não for Fracao, retorne NotImplemented.
#
# Teste você mesmo: no fim do arquivo, crie as frações e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que Fracao(1, 0) é recusada.
#
# SE TRAVAR, REVEJA:
#   __add__ ................ aula 07, slide 25  https://poo.leoad.com.br/aulas/aula-07/#s25
#   NotImplemented ......... aula 07, slide 30  https://poo.leoad.com.br/aulas/aula-07/#s30
#   __lt__ e __len__ ....... aula 07, slide 36  https://poo.leoad.com.br/aulas/aula-07/#s36
#   recusa no __init__ ..... aula 04, slide 21  https://poo.leoad.com.br/aulas/aula-04/#s21
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
