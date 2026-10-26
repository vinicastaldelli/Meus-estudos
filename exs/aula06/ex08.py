# Aula 06 · Exercício 08 (casa, desafio): a biblioteca
#
# ItemAcervo: o __init__ recebe titulo e ano; todo item nasce com emprestado = False.
#   titulo        @property SÓ DE LEITURA (guarde em self._titulo).
#   prazo_dias()  RETORNA 7.
#   emprestar()   muda emprestado para True. Se o item JÁ estiver emprestado,
#                 RECUSA:  raise ValueError("item já emprestado")
#   __str__       retorna, por exemplo:  Mapa de Goiás (2020), prazo de 7 dias
#                 (use self.prazo_dias() no texto)
#
# Livro é um ItemAcervo com autor (__init__ com super()).
#   prazo_dias()  SUBSTITUI: 14.
# Revista é um ItemAcervo.
#   prazo_dias()  ESTENDE: o prazo do pai menos 4.
#
# Acervo NÃO herda de ItemAcervo: um acervo não é um item, ele TEM itens.
#   O __init__ recebe nome e cria self.itens = [].
#   adicionar(item)   coloca o item na lista.
#   disponiveis()     RETORNA quantos itens não estão emprestados.
#   quantos_livros()  RETORNA quantos itens são Livro (use isinstance).
#   maior_prazo()     RETORNA o item com o maior prazo_dias(), ou None se a lista estiver vazia.
#
# Exemplo: um ItemAcervo, um Livro emprestado e uma Revista no acervo:
#   disponiveis() retorna 2, quantos_livros() retorna 1, e o print do maior_prazo() mostra
#   Dom Casmurro (1899), prazo de 14 dias
#
# Teste você mesmo: no fim do arquivo, monte o acervo do exemplo e mostre
# os resultados com print. Mostre também, com try/except, que emprestar o
# mesmo livro duas vezes é recusado.
#
# SE TRAVAR, REVEJA:
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class ItemAcervo:
    def __init__(self, titulo, ano, emprestado = False):
        self._titulo = titulo
        self.ano = ano
        self.emprestado = emprestado

    @property
    def titulo(self):
        return self._titulo

    def prazo_dias(self):
        return 7

    def emprestar(self):
        if self.emprestado:
            raise ValueError("item já emprestado")
        self.emprestado = True

    def __str__(self):
        return f"{self.titulo} ({self.ano}), prazo de {self.prazo_dias} dias"

class Livro(ItemAcervo):
    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.autor = autor

    def prazo_dias(self):
        return 14

class Revista(ItemAcervo):
    def prazo_dias(self):
        return super().prazo_dias() - 4

class Acervo:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        return self.itens.append(item)

    def disponiveis(self):
        disponivel = 0
        for item in self.itens:
            if not item.emprestado:
                disponivel += 1
        return disponivel

    def quantos_livros(self):
        quantidade = 0
        for item in self.itens:
            if isinstance(item, Livro):
                quantidade += 1
        return quantidade

    def maior_prazo(self):
        if not self.itens:
            return None
        maior = self.itens[0]
        for item in self.itens[1:]:
            if item.prazo_dias() > maior.prazo_dias():
                maior = item
            return maior

acervo = Acervo("Biblioteca")

item = ItemAcervo("Item avulso", 2020)
livro = Livro("Dom Casmurro", 1899, "Machado de Assis")
revista = Revista("Revista Exemplo", 2024)

livro.emprestar()

acervo.itens.extend([item, livro, revista])

print("Disponíveis:", acervo.disponiveis())
print("Livros:", acervo.quantos_livros())

maior = acervo.maior_prazo()
if maior is not None:
    print(f"{maior.titulo} ({maior.ano}), prazo de {maior.prazo_dias()} dias")

try:
    livro.emprestar()
except ValueError as erro:
    print(f"Empréstimo recusado: {erro}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# Disponíveis: 2
# Livros: 1
# Dom Casmurro (1899), prazo de 14 dias
# Empréstimo recusado: item já emprestado