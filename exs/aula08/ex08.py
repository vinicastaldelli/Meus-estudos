# Aula 08 · Exercício 08 (casa, desafio): a batalha de personagens
#
# Crie a classe abstrata Personagem (herda de ABC):
#   __init__(nome)    guarda o nome; todo personagem começa com vida 100.
#   vida              property concreta com setter que CORRIGE o valor:
#                     abaixo de 0 vira 0, acima de 100 vira 100.
#                     Guarde em self._vida.
#   dano              property ABSTRATA: quanto o ataque tira.
#   atacar(alvo)      concreto: tira self.dano da vida do alvo e RETORNA:
#                     Thor ataca Merlin: Merlin fica com 85 de vida
#   descansar()       concreto: soma 10 na vida (o setter segura no 100).
#   esta_vivo()       concreto: RETORNA True se a vida for maior que 0.
#
# E as duas filhas:
# Guerreiro   dano 15.
# Mago        o __init__ recebe nome e mana: chame super().__init__(nome)
#             e guarde self.mana. Dano 25 se tiver 10 de mana ou mais,
#             senão 5. O Mago ESTENDE o atacar(): chama o atacar() do pai
#             com super(), depois gasta 10 de mana (se tiver 10 ou mais)
#             e retorna o mesmo texto do pai.
#
# Fora das classes, a função batalha(a, b): a ataca b, depois b ataca a,
# e assim por diante, imprimindo cada ataque. Depois de CADA ataque, se
# quem apanhou morreu, a batalha acaba ali (o morto não ataca de volta).
# RETORNA o nome de quem ficou vivo.
#
# Exemplos:
#   thor = Guerreiro("Thor")
#   merlin = Mago("Merlin", 30)
#   thor.atacar(merlin)    Thor ataca Merlin: Merlin fica com 85 de vida
#   merlin.atacar(thor)    Merlin ataca Thor: Thor fica com 75 de vida
#   merlin.mana            20
#   thor.descansar()       a vida do Thor vai para 85
#   batalha(Guerreiro("Thor"), Mago("Merlin", 30))   retorna Thor
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   property abstrata ...... aula 08, slide 21  https://poo.leoad.com.br/aulas/aula-08/#s21
#   setter ................. aula 03, slide 18  https://poo.leoad.com.br/aulas/aula-03/#s18
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25

from abc import ABC, abstractmethod


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
