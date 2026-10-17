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

class Horario:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    @property
    def hora(self):
        return self._hora
    
    @hora.setter
    def hora(self, valor):
        if 0 <= valor <= 23:
            self._hora = valor
        else:
            raise ValueError("Hora deve estar entre 0 e 23.")

    @property
    def minuto(self):
        return self._minuto
    
    @minuto.setter
    def minuto(self, valor):
        if 0 <= valor <= 59:
            self._minuto = valor
        else:
            raise ValueError("Minuto deve estar entre 0 e 59.")

    def avancar(self, minutos):
        total_minutos = self.hora * 60 + self.minuto + minutos
        self.hora = (total_minutos // 60) % 24
        self.minutos = total_minutos % 60

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"       

horario1 = Horario(8, 50)
print(horario1)
horario1.avancar(25)
print(horario1)

horario2 = Horario(23, 50)
print(horario2)
horario2.avancar(15)
print(horario2)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# 08:50
# 09:50
# 23:50
# 00:50