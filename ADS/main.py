# from Pessoa import Pessoa

# p1 = Pessoa('Luiz', 30)
# p2 = Pessoa('Maria', 25)

# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

p1 = Pessoa.por_ano_nascimento('Luiz', 1964)

print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(p1.idade)
