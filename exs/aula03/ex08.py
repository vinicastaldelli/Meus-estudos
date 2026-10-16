# Aula 03 · Exercício 08 (casa, desafio): a classe Horario
#
# O __init__ recebe hora e minuto e guarda os dois PELOS SETTERS.
# hora      @property com setter que RECUSA fora de 0 a 23 (raise ValueError).
# minuto    @property com setter que RECUSA fora de 0 a 59 (raise ValueError).
# avancar(minutos)   anda o relógio. 08:50 avançando 25 vira 09:15;
#                    23:50 avançando 15 vira 00:05.
#                    Dica: transforme tudo em minutos, some, e use // 60 e % 60
#                    (aula 01); para a hora não passar de 23, use % 24.
# __str__   retorna sempre com 2 dígitos, por exemplo: 08:05
#           (número menor que 10 ganha um "0" na frente).
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print, incluindo a virada da meia-noite. Se quiser ver a
# recusa, deixe essa tentativa como ÚLTIMA linha: o programa para no seu
# ValueError e o que vem depois não roda.

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
