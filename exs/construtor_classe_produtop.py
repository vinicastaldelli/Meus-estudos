class ContaPoupanca:
    taxa = 0.05                    # atributo de classe: um só, de todas as contas
    total_contas = 0               # contador: também é da classe

    def __init__(self, titular, saldo=0, historico=None):    # valores padrão
        if historico is None:      # lista como padrão: None, nunca []
            historico = []
        self._titular = titular    # só de leitura: grava direto no _ (aula 03)
        self.saldo = saldo         # tem setter: passa por ele (aula 04)
        self.historico = historico
        ContaPoupanca.total_contas = ContaPoupanca.total_contas + 1    # pela classe

    @property
    def titular(self):             # getter, sem setter: só de leitura (aula 03)
        return self._titular

    @property
    def saldo(self):               # getter (aula 03)
        return self._saldo

    @saldo.setter
    def saldo(self, valor):        # setter que recusa (aula 04)
        if valor < 0:
            raise ValueError("saldo não pode ser negativo")
        self._saldo = valor

    @classmethod
    def de_texto(cls, texto):      # construtor alternativo: cls é a classe
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))

    def render(self):
        ganho = self.saldo * self.taxa    # self.taxa: não está no objeto, vem da classe
        self.saldo = self.saldo + ganho   # passa pelo setter de novo
        self.historico.append(ganho)

    def __repr__(self):            # (aula 02)
        return f"ContaPoupanca('{self.titular}', {self.saldo})"

ana = ContaPoupanca("Ana", 1000)
bia = ContaPoupanca.de_texto("Bia;200")
caio = ContaPoupanca("Caio")

ana.render()
print([ana, bia, caio])                # [ContaPoupanca('Ana', 1050.0), ContaPoupanca('Bia', 200.0), ContaPoupanca('Caio', 0)]
print(ana.historico, caio.historico)   # [50.0] []
print(ContaPoupanca.total_contas)      # 3