# Aula 09 · Exercício 07 (casa, opcional): o sensor de temperatura
#
# Escreva a classe Sensor do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex07-sensor.svg
# limite e total     sublinhados: atributos de classe. total conta os
#                    sensores criados.
# temperatura        @property com setter. O setter RECUSA menos de -50:
#                        raise ValueError("temperatura impossível")
#                    e só depois guarda em self._temperatura.
# de_texto           @classmethod. Recebe "Cozinha;42.5".
# alerta()           RETORNA True se a temperatura passou do limite.
# __str__            Cozinha: 42.5 graus
# __repr__           Sensor('Cozinha', 42.5)
#
# Teste você mesmo: no fim do arquivo, crie sensores (um pelo de_texto),
# mostre o alerta de cada um e provoque a recusa dentro de um try/except.
#
# SE TRAVAR, REVEJA:
#   a caixa da classe ...... aula 09, slide 8  https://poo.leoad.com.br/aulas/aula-09/#s8
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27

class Sensor:
    limite = 40
    total = 0
    
    def __init__(self, local, temperatura):
        self.local = local
        self.temperatura = temperatura
        Sensor.total += 1

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -50:
            raise ValueError("temperatura impossível")
        self._temperatura = valor

    @classmethod
    def de_texto(cls, texto):
        local, temperatura = texto.split(";")
        return cls(local, float(temperatura))

    def alerta(self):
        return self.temperatura > self.limite

    def __str__(self):
        return f"{self.local}: {self.temperatura:.2f} graus"

    def __repr__(self):
        return f"Sensor('{self.local}', {self.temperatura:.2f})"

sensor1 = Sensor("Estufa", 45)
sensor2 = Sensor.de_texto("Sala;32")

print(f"{sensor1}: alerta = {sensor1.alerta()}")
print(f"{sensor2}: alerta = {sensor2.alerta()}")

try:
    sensor_recusado = Sensor("Congelador", -60)
except ValueError as erro:
    print(f"Sensor recusado: {erro}")

print(f"Total de sensores criados: {Sensor.total}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# Estufa: 45.00 graus: alerta = True
# Sala: 32.00 graus: alerta = False
# Sensor recusado: temperatura impossível
# Total de sensores criados: 2