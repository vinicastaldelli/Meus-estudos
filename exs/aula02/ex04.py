# Aula 02 · Exercício 04 (casa, OBRIGATÓRIO): a classe Carro
#
# O __init__ recebe marca, modelo e ano.
# descricao()        RETORNA, por exemplo: Fiat Uno (2010)
# idade(ano_atual)   RETORNA quantos anos o carro tem.
# __str__            retorna o mesmo texto da descricao(), chamando self.descricao().
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

    def idade(self, ano_atual):
        return ano_atual - self.ano

    def __str__(self):
        return self.descricao()

c1 = Carro("Cronos", "Fiat", 2018)
c2 = Carro("Ka", "Ford", 2013)

print(c1, c1.idade(2026), "anos")
print(c2, c2.idade(2026), "anos")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# Cronos Fiat (2018) 8 anos
# Ka Ford (2013) 13 anos