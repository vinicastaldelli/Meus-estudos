class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def andar(self):
        print(f"{self.nome} está andando: ")
    
    def falar(self):
        print(f"{self.nome} está falando: ")

pessoa1 = Pessoa("João", 14)

print(f"Nome: {pessoa1.nome} \nIdade: {pessoa1.idade}")

pessoa1.andar()
pessoa1.falar()
