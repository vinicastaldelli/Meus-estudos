# Aula 10 · Exercício 07 (casa, opcional): a agenda de contatos
#
# Crie a classe Contato. O __init__ recebe nome e telefone e guarda os dois.
#   __repr__  retorna, por exemplo: Contato('Ana', '62 99999-0001')
#
# Crie a classe Agenda, que guarda os contatos num dicionário (a chave é o
# nome, o valor é o objeto Contato). O dicionário nasce vazio no __init__.
#   adicionar(contato)  guarda o contato. Se o nome já existir, levanta
#                       ValueError com a mensagem: contato repetido: Ana
#   buscar(nome)        RETORNA o contato, ou None se o nome não existir.
#   remover(nome)       apaga e RETORNA True; se o nome não existir, RETORNA False.
#   listar()            RETORNA a lista dos contatos em ordem alfabética de
#                       nome. Use sorted sobre os valores, com key=lambda.
#
# Exemplo: depois de adicionar Caio, Ana e Bia, nessa ordem,
#   listar()         retorna [Contato('Ana', '62 99999-0001'), Contato('Bia', '62 99999-0002'), Contato('Caio', '62 99999-0003')]
#   buscar("Duda")   retorna None
#   remover("Caio") retorna True; chamando de novo, retorna False
#   adicionar outro contato chamado Ana: ValueError: contato repetido: Ana
#
# Teste você mesmo: no fim do arquivo, crie a agenda, mostre os resultados
# com print e use try/except para mostrar a mensagem do contato repetido.
#
# SE TRAVAR, REVEJA:
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   except ... as erro ..... aula 04, slide 15  https://poo.leoad.com.br/aulas/aula-04/#s15
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   dicionário no __init__ . aula 10, slide 42  https://poo.leoad.com.br/aulas/aula-10/#s42
#   sorted com key ......... aula 10, slide 19  https://poo.leoad.com.br/aulas/aula-10/#s19
#   lambda ................. aula 10, slide 24  https://poo.leoad.com.br/aulas/aula-10/#s24

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"Contato('{self.nome}', '{self.telefone}')"

class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, contato):
        if contato.nome in self.contatos:
            raise ValueError(f"contato repetido: {contato.nome}")
        self.contatos[contato.nome] = contato

    def buscar(self, nome):
        return self.contatos.get(nome)

    def remover(self, nome):
        if nome not in self.contatos:
            return False
        del self.contatos[nome]
        return True

    def listar(self):
        return sorted(self.contatos.values(), key=lambda contato: contato.nome)

agenda = Agenda()

agenda.adicionar(Contato("Caio", "62 99999-0003"))
agenda.adicionar(Contato("Ana", "62 99999-0001"))
agenda.adicionar(Contato("Bia", "62 99999-0002"))

print("Contatos:", agenda.listar())
print('Buscar Duda:', agenda.buscar("Duda"))
print('Remover Caio:', agenda.remover("Caio"))
print('Remover Caio novamente:', agenda.remover("Caio"))

try:
    agenda.adicionar(Contato("Ana", "62 98888-0000"))
except ValueError as erro:
    print(erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# Contatos: [Contato('Ana', '62 99999-0001'), Contato('Bia', '62 99999-0002'), Contato('Caio', '62 99999-0003')]
# Buscar Duda: None
# Remover Caio: True
# Remover Caio novamente: False
# contato repetido: Ana