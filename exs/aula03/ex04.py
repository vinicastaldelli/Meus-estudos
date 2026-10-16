# Aula 03 · Exercício 04 (casa, OBRIGATÓRIO): a classe Temperatura
#
# O __init__ recebe celsius e guarda PELO SETTER: self.celsius = celsius.
# celsius      @property: RETORNA o valor guardado em self._celsius.
#              @celsius.setter: RECUSA valor abaixo de -273 com
#              raise ValueError("Abaixo do zero absoluto")
# fahrenheit   @property calculada, só de leitura: RETORNA celsius * 1.8 + 32
# __str__      retorna, por exemplo: 25 °C = 77.0 °F
#              A conta pode sair com muitas casas (36.6 dá 97.88000000000001):
#              no __str__, mostre o fahrenheit com 1 casa, com :.1f.
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos, mostre
# os resultados com print e mude o celsius de um deles. Como ÚLTIMA linha,
# tente gravar -300: o programa tem que parar com o seu ValueError.

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273:
            raise ValueError("Abaixo de zero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 1.8 +32

    def __str__(self):
        return f"{self._celsius} ºC = {self.fahrenheit:.1f} ºF"


t1 = Temperatura(25)
t2 = Temperatura(-10)
print(t1)
print(t2)
print(t1.fahrenheit)
t1.celsius = 30
print(t1)
t1.celsius = -300


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# 25 ºC = 77.0 ºF
# -10 ºC = 14.0 ºF
# 77.0
# 30 ºC = 86.0 ºF
# Traceback (most recent call last):
#   File "c:\Meus-estudos\exs\aula03\ex04.py", line 45, in <module>
#     t1.celsius = -300
#     ^^^^^^^^^^
#   File "c:\Meus-estudos\exs\aula03\ex04.py", line 27, in celsius
#     raise ValueError("Abaixo de zero absoluto")
# ValueError: Abaixo de zero absoluto