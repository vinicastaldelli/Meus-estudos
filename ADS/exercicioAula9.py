class Manuntencao:
    def __init__(self, descrição, responsavel, custo, status="Aberta"):
        # Atributos privados
        self.__descrição = None
        self.__responsavel = None
        self.__custo = None
        self.__stauts = None

        # Atribuição passando pelas validações dos setters
        self.descrição = descrição
        self.__responsavel = responsavel
        self.custo = custo
        self.stauts = status

        @property
        def descricao(self):
            return self.__descricao
        
        @descricao.setter
        def descricao(self, valor):
            if not valor or not str(valor).strip():
