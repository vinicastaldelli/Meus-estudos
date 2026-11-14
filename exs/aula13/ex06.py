# Aula 13 · Exercício 06 (casa, opcional): o sensor que avisa
#
# Sensor: o __init__ recebe local, guarda com self e cria duas coisas:
#   self.ultima = None   (a última temperatura medida)
#   self.avisos = []     (uma lista de FUNÇÕES)
#   inscrever(funcao)    guarda a função na lista, sem chamar.
#   medir(temperatura)   guarda a temperatura em self.ultima e chama CADA função
#                        da lista, passando a temperatura.
#
# Escreva também três funções que recebem a temperatura t:
#   alerta_calor(t)   se t for maior que 30, imprime:  Calor! 35 graus
#   alerta_frio(t)    se t for menor que 10, imprime:  Frio! 8 graus
#   painel(t)         sempre imprime:                  Painel: 22 graus
#
# Exemplo: um Sensor("Estufa") com as três inscritas (sem parênteses!).
#   medir(35) mostra   Calor! 35 graus   e depois   Painel: 35 graus
#   medir(22) mostra só   Painel: 22 graus
#   Depois das medições, self.ultima vale a última temperatura medida.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   f × f() ................ aula 10, slide 8  https://poo.leoad.com.br/aulas/aula-10/#s8
#   callback ............... aula 13, slide 29  https://poo.leoad.com.br/aulas/aula-13/#s29
#   Observer ............... aula 13, slide 31  https://poo.leoad.com.br/aulas/aula-13/#s31

class Sensor:
    def __init__(self, local):
        self.local = local
        self.ultima = None
        self.avisos = []

    def inscrever(self, funcao):
        self.avisos.append(funcao)

    def medir(self, temperatura):
        self.ultima = temperatura
        for aviso in self.avisos:
            aviso(temperatura)

def alerta_calor(t):
    if t > 30:
        print(f"Calor! {t} graus")

def alerta_frio(t):
    if t < 10:
        print(f"Frio! {t} graus")

def painel(t):
    print(f"Painel: {t} graus")

sensor = Sensor("Estufa")
sensor.inscrever(alerta_calor)
sensor.inscrever(alerta_frio)
sensor.inscrever(painel)

sensor.medir(35)
sensor.medir(8)
sensor.medir(22)

print("Última:", sensor.ultima)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# Calor! 35 graus
# Painel: 35 graus
# Frio! 8 graus
# Painel: 8 graus
# Painel: 22 graus
# Última: 22