class Funcionario:                                  # o pai: o que é comum
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def bonus(self):
        return self.salario * 0.10

    def __str__(self):
        return f"{self.nome}, bônus R$ {self.bonus():.2f}"    # self.bonus(): a versão do objeto

class Estagiario(Funcionario):                      # é um Funcionario
    def bonus(self):                                # SUBSTITUI: o pai não roda
        return 300

class Gerente(Funcionario):                         # é um Funcionario
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)             # o pai guarda nome e salário
        self.setor = setor                          # a filha guarda o que é dela

    def bonus(self):                                # ESTENDE: o pai roda e a filha soma
        return super().bonus() + 250

    def __str__(self):                              # ESTENDE o texto do pai
        return f"{super().__str__()} (gerente de {self.setor})"

equipe = [Funcionario("Caio", 4000), Estagiario("Duda", 1500), Gerente("Ana", 10000, "Vendas")]
for pessoa in equipe:
    print(pessoa)
print(isinstance(equipe[2], Funcionario))

# Caio, bônus R$ 400.00
# Duda, bônus R$ 300.00
# Ana, bônus R$ 1250.00 (gerente de Vendas)
# True