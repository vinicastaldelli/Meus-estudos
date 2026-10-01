class Loja:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo")
        
        self.__preco = novo_preco
        print("Preço cadastrado/alterado com sucesso!")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == "":
            raise ValueError("O nome não pode ser vazio")
        self.__nome = novo_nome
        print("Nome cadastrado/alterado com sucesso!")

    def exibir_informacao(self):
        print("Nome do Produto:", self.nome)
        print("Preço do Produto:", self.preco)

try:
    produto = Loja("Mouse", 50)
    produto.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

# testando a regra
try:
    produto.preco = -500
    produto.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)

print("\nTestando com valor válido")
try:
    produto.preco = 100
    produto.nome = "Teclado"
    produto.exibir_informacao()
except ValueError as erro:
    print("Erro:", erro)
