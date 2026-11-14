# Aula 13 · Exercício 08 (casa, desafio): o placar que avisa
#
# Jogo: o __init__ recebe casa e visitante (os nomes dos dois times), guarda
# os dois com self e cria:
#   self.placar = {casa: 0, visitante: 0}   (um dicionário: time -> gols)
#   self.inscritos = []                     (os interessados no placar)
#   texto()          RETORNA o placar, por exemplo:  Vila Nova 4 x 1 Goiás
#   inscrever(f)     guarda f na lista de inscritos, sem chamar.
#   gol(time)        soma 1 no placar desse time e chama CADA inscrito,
#                    passando self.texto().
#
# Os inscritos são MÉTODOS de objetos (sem parênteses!):
#   Narrador: o __init__ recebe nome.
#     avisar(placar)   imprime, por exemplo:   Rádio: Vila Nova 1 x 0 Goiás
#   Telao: o __init__ cria self.vezes = 0.
#     mostrar(placar)  soma 1 em self.vezes e imprime:   [TELÃO] Vila Nova 1 x 0 Goiás
#
# Exemplo:
#   jogo = Jogo("Vila Nova", "Goiás"), um Narrador("Rádio") e um Telao().
#   jogo.inscrever(radio.avisar) e jogo.inscrever(telao.mostrar).
#   jogo.gol("Vila Nova") mostra:
#     Rádio: Vila Nova 1 x 0 Goiás
#     [TELÃO] Vila Nova 1 x 0 Goiás
#   Depois de mais três gols do Vila Nova e um do Goiás, jogo.texto() é
#   Vila Nova 4 x 1 Goiás, e telao.vezes vale 5.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   dicionário ............. aula 10, slide 33  https://poo.leoad.com.br/aulas/aula-10/#s33
#   Observer ............... aula 13, slide 31  https://poo.leoad.com.br/aulas/aula-13/#s31
#   método inscrito ........ aula 13, slide 32  https://poo.leoad.com.br/aulas/aula-13/#s32


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
