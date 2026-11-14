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

class Jogo:
    def __init__(self, casa, visitante):
        self.casa = casa
        self.visitante = visitante
        self.placar = {casa: 0, visitante: 0}
        self.inscritos = []

    def texto(self):
        return (f"{self.casa} {self.placar[self.casa]} x "
        f"{self.placar[self.visitante]} {self.visitante}")

    def inscrever(self, f):
        self.inscritos.append(f)

    def gol(self, time):
        self.placar[time] += 1
        placar_atual = self.texto()
        for f in self.inscritos:
            f(placar_atual)

class Narrador:
    def __init__(self, nome):
        self.nome = nome

    def avisar(self, placar):
        print(f"{self.nome}: {placar}")

class Telao:
    def __init__(self):
        self.vezes = 0

    def mostrar(self, placar):
        self.vezes += 1
        print(f"[TELÃO] {placar}")

jogo = Jogo("Vila Nova", "Goiás")
radio = Narrador("Rádio")
telao = Telao()
jogo.inscrever(radio.avisar)
jogo.inscrever(telao.mostrar)
jogo.gol("Vila Nova")
for _ in range(3):
    jogo.gol("Vila Nova")
jogo.gol("Goiás")
print(jogo.texto())
print(telao.vezes)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# Rádio: Vila Nova 1 x 0 Goiás
# [TELÃO] Vila Nova 1 x 0 Goiás
# Rádio: Vila Nova 2 x 0 Goiás
# [TELÃO] Vila Nova 2 x 0 Goiás
# Rádio: Vila Nova 3 x 0 Goiás
# [TELÃO] Vila Nova 3 x 0 Goiás
# Rádio: Vila Nova 4 x 0 Goiás
# [TELÃO] Vila Nova 4 x 0 Goiás
# Rádio: Vila Nova 4 x 1 Goiás
# [TELÃO] Vila Nova 4 x 1 Goiás
# Vila Nova 4 x 1 Goiás
# 5