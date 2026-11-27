from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, placa, horas, id=None):
        self.id = id
        self.placa = placa
        self.horas = horas

    @abstractmethod
    def valor(self):
        pass

    @classmethod
    def from_row(cls, linha):
        id, tipo, placa, horas = linha
        return cls(placa, horas, id)


class Carro(Veiculo):
    tipo = "carro"

    def valor(self):
        return self.horas * 5


class Moto(Veiculo):
    tipo = "moto"

    def valor(self):
        return self.horas * 3


TIPOS = {"carro": Carro, "moto": Moto}    # texto da coluna tipo -> CLASSE


def criar_veiculo(linha):
    tipo = linha[1]
    if tipo not in TIPOS:
        raise ValueError(f"tipo desconhecido: {tipo}")
    classe = TIPOS[tipo]
    return classe.from_row(linha) 


linhas = [(1, "moto", "XYZ9K87", 4), (2, "carro", "ABC1D23", 2), (3, "moto", "QWE4R56", 1)]
patio = [criar_veiculo(linha) for linha in linhas]

print(patio[0].tipo, patio[0].valor())    # moto 12
print(patio[1].id, patio[1].valor())      # 2 10
print(TIPOS["moto"])                      # <class '__main__.Moto'>

mensagem = "nenhum erro"
try:
    criar_veiculo((4, "bicicleta", "SEM0000", 1))
except ValueError as erro:
    mensagem = str(erro)
print(mensagem)                           # tipo desconhecido: bicicleta

total = sum([v.valor() for v in patio])
print(f"chave: {patio[2].tipo}-{patio[2].id}-{total}-{len(mensagem)}")