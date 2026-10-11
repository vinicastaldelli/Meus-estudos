# Aula 02 · Exercício 06 (casa, opcional): a classe Temperatura
#
# O __init__ recebe celsius.
# para_fahrenheit()  RETORNA celsius * 1.8 + 32
# __str__            retorna, por exemplo: 25.0 °C = 77.0 °F  (1 casa decimal: :.1f)
# __repr__           retorna, por exemplo: Temperatura(25)
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def para_fahrenheit(self):
        return self.celsius * 1.8 + 32

    def __str__(self):
        return f"{self.celsius} °C = {self.para_fahrenheit():.1f} °F"

    def __repr__ (self):
        return F"Temperatura({self.celsius})"

t1 = Temperatura(25)
t2 = Temperatura(0)

print(t1)
print(repr(t1))
print(t2)
print(repr(t2))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# 25 °C = 77.0 °F
# Temperatura(25)
# 0 °C = 32.0 °F
# Temperatura(0)