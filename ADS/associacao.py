class tecnico:
    def __init__(self, nome):
        self. nome = nome

    def realizar_manutencao(self, equipamento):
        print (f"O tecnico {self.nome} está realizando a manutenção do equipamento {equipamento.nome}")

class equipamento:
    def __init__(self, tecnico):
        print(f"O equipamento {self.nome} está com o tecnico {tecnico.nome}")

class especificacao:
    def __init__(self, descricao):
        self.descricao = descricao

    def especificacao(self):
        print(f"O equipamento te a seguinte especificacao: {self.descricao}")

tecnico1 = tecnico("Vinícius")
tecnico2 = tecnico("fdp")

equipamento1 = equipamento("MacBook Air")
equipamento2 = equipamento("projetor Sansung")

especificacao1 = especificacao("13 polegadas, 16GB de RAM")
especificacao2 = especificacao("1200 lumens, 1024x768 resoluçao")

tecnico1.realizar_manutencao(equipamento2)
tecnico2.realizar_manutencao(equipamento2)
