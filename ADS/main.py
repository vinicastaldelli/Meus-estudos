from random import randint
# from Pessoa import Pessoa

# p1 = Pessoa('Luiz', 30)
# p2 = Pessoa('Maria', 25)

# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())

# class Pessoa:
#     ano_atual = 2026

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def get_ano_nascimento(self):
#         print(self.ano_atual - self.idade)

#     @classmethod
#     def por_ano_nascimento(cls, nome, ano_nascimento):
#         idade = cls.ano_atual - ano_nascimento
#         return cls(nome, idade)
    
#     @staticmethod
#     def gera_id():
#         rand = randint(10000, 19999)
#         return rand
# p1 = Pessoa.por_ano_nascimento('Luiz', 1964)

# print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
# print(Pessoa.gera_id())
# print(p1.gera_id())

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@').title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)