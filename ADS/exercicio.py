class Manutenção:
    def __init__(self, descricao, responsavel, custo, status):
        self.descricao = descricao
        self.responsavel = responsavel
        self.custo = custo
        self.status = status

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if nova_descricao == "":
            raise ValueError("A descrição não pode ser vazia")
        self.__descricao = nova_descricao
        print("Descrição cadastrada/alterada com sucesso!")

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, novo_responsavel):
        if novo_responsavel == "":
            raise ValueError("O responsável não pode ser vazio")
        self.__responsavel = novo_responsavel
        print("Responsável cadastrado/alterado com sucesso!")

    @property
    def custo(self):
            return self.__custo
    
    @custo.setter
    def custo(self, novo_custo):
            if novo_custo < 0:
                raise ValueError("O custo não pode ser negativo")
            self.__custo = novo_custo
            print("Custo cadastrado/alterado com sucesso!")

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        if novo_status != "Aberta" and novo_status != "Em andamento" and novo_status != "Concluída":
            raise ValueError("O status deve ser 'Aberta', 'Em andamento' ou 'Concluída'")
        self.__status = novo_status
        print("Status cadastrado/alterado com sucesso!")


    def exibir_informacao(self):
        print("Descrição:", self.descricao)
        print("Responsável:", self.responsavel)
        print("Custo:", self.custo)
        print("Status:", self.status)

try:
    manutencao = Manutenção("Troca de peça", "João", 100, "Aberta")
    manutencao.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

# testando a regra
print("\nTestando com custo inválido")
try:
    manutencao.custo = -500
    manutencao.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

print("\nTestando com custo válido")
try:
    manutencao.custo = 150
    manutencao.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

print("\nTestando com responsavel vazio")
try:
    manutencao.responsavel = ""
    manutencao.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

print("\nTestando com status vazio")
try:
    manutencao.status = ""
    manutencao.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)
