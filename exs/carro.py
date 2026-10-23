class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        self.ligado = True


class Motorista:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    total_carros = 0                         # atributo de classe (hoje)

    def __init__(self, modelo, potencia, motorista, quilometragem=0):    # valor padrão (hoje)
        self._modelo = modelo                # só de leitura: grava direto no _ (aula 03)
        self.motor = Motor(potencia)         # composição: o carro CRIA o motor (hoje)
        self.motorista = motorista           # associação: recebe o motorista pronto (hoje)
        self.quilometragem = quilometragem   # tem setter: passa por ele (aula 04)
        Carro.total_carros = Carro.total_carros + 1    # pela classe (hoje)

    @property
    def modelo(self):                        # getter, sem setter: só de leitura (aula 03)
        return self._modelo

    @property
    def quilometragem(self):                 # getter (aula 03)
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):          # setter que recusa (aula 04)
        if valor < 0:
            raise ValueError("quilometragem não pode ser negativa")
        self._quilometragem = valor

    def rodar(self, km):
        self.motor.ligar()                   # o carro pede ao motor
        self.quilometragem = self.quilometragem + km    # passa pelo setter de novo

    def __repr__(self):                      # (aula 02)
        return f"Carro('{self.modelo}', {self.quilometragem} km, {self.motorista.nome})"


ana = Motorista("Ana")
uno = Carro("Uno", 75, ana)
gol = Carro("Gol", 80, ana, 12000)

uno.rodar(150)
print([uno, gol])                            # [Carro('Uno', 150 km, Ana), Carro('Gol', 12000 km, Ana)]
print(uno.motor.ligado, gol.motor.ligado)    # True False
print(Carro.total_carros)                    # 2