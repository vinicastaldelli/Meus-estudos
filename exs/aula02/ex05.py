# Aula 02 · Exercício 05 (casa, OBRIGATÓRIO): a classe Retangulo
#
# O __init__ recebe largura e altura.
# area()          RETORNA largura vezes altura.
# perimetro()     RETORNA 2 vezes (largura + altura).
# eh_quadrado()   RETORNA True se largura e altura forem iguais, senão False.
# __str__         retorna, por exemplo: Retângulo 4x3 | área 12 | perímetro 14
#                 (use self.area() e self.perimetro())
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def eh_quadrado(self):
        if self.largura == self.altura:
            return True
        return False

    def __str__(self):
        return f"Retângulo {self.largura} x {self.altura} | área {self.area()} / perímetro {self.perimetro()}"

r1 = Retangulo(68, 47)
print(r1)
r2 = Retangulo(78, 35)
print(r2)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# Retângulo 68 x 47 | área 3196 / perímetro 230
# Retângulo 78 x 35 | área 2730 / perímetro 226