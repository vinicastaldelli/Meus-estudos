class Moto:
    def __init__(self, placa):
        self.placa = placa

    def tarifa(self, horas):
        return horas * 3

class Carro:
    def __init__(self, placa):
        self.placa = placa

    def tarifa(self, horas):
        return horas * 5

class Caminhao:
    def __init__(self, placa):
        self.placa = placa
    
    def tarifa(self, horas):
        return horas * 10
# 1. Crie aqui a classe Caminhao: igual às outras, mas a tarifa é horas * 10

VEICULOS = {"moto": Moto, "carro": Carro, "caminhao": Caminhao}    # 2. registre o caminhão nesta linha

def entrar(tipo, placa):
    return VEICULOS[tipo](placa)

patio = [entrar("carro", "ABC1D23"), entrar("caminhao", "CAM2E45"), entrar("moto", "XYZ9K87")]

total = 0

for veiculo in patio:
    total += veiculo.tarifa(2)
# 3. com um for, some em total a tarifa de 2 horas de cada veículo do pátio

print(total)
print(f"chave: {total}-{entrar('caminhao', 'BRA2E19').tarifa(3)}-{len(VEICULOS)}")