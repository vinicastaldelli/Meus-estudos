class Profissional:
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade

    def calcular_custo(self, horas: int, valor: float) -> float:
        return horas * valor

class Equipamento:
    def __init__(self, marca: str, modelo: str, patrimonio: str, data_fabricação: str):
        self.marca = marca
        self.modelo = modelo
        self.patrimonio = patrimonio
        self.data_fabricação = data_fabricação

class Técnico:
    def __init__(self, nome: str, patrimonio: str, setor: str):
        self.nome = nome
        self.patrimonio = patrimonio
        self.setor = setor

class Manutenção:
    def __init__(self, status: str, tipoManutenção: str, equipamento: Equipamento, técnico: Técnico):
        self.status = status
        self.tipoManutenção = tipoManutenção
        self.equipamento = equipamento
        self.técnico = técnico
    
