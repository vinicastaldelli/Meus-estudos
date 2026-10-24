# Aula 06 · Exercício 09 (grande): o estacionamento do shopping
#
# Um exercício maior, com tudo o que vimos das aulas 01 a 06. Faça por
# partes, na ordem, rodando a cada parte. O teste também está dividido por
# partes: quando ele parar com erro numa parte que você ainda não fez, é
# esperado. As linhas de cima continuam mostrando o que você já fez.
# Entrega até quinta, 29/10, às 18h35 (início da aula 07).
# Depois disso, não é aceito.
#
# PARTE 1 · A exceção e o veículo
#   EstacionamentoLotadoError: uma exceção própria (filha de Exception).
#   Veiculo tem dois atributos de classe:
#     tarifa_hora = 6.0    o preço da hora, igual para todo veículo
#     total = 0            conta quantos veículos foram criados
#   O __init__ recebe placa, modelo e horas, com horas = 1 como valor padrão.
#   O total só aumenta (pela classe: Veiculo.total) DEPOIS que tudo foi
#   guardado: veículo recusado não conta.
#
# PARTE 2 · As properties
#   placa  @property só de leitura (sem setter): o __init__ grava self._placa.
#   horas  @property e @horas.setter. O setter RECUSA menos de 1 hora:
#              raise ValueError("o mínimo é 1 hora")
#          O __init__ faz self.horas = horas: o setter roda na criação.
#
# PARTE 3 · Texto e construtor alternativo
#   valor()    RETORNA self.tarifa_hora vezes as horas.
#   __str__    RETORNA, por exemplo:  ABC1D23 Gol · 3h · R$ 18.00
#              (use self.valor() no texto, com :.2f)
#   __repr__   RETORNA, por exemplo:  Veiculo('UNO2E34', 'Uno', 1)
#   de_texto   @classmethod: recebe "HBV5F67;HB20;2" e RETORNA o veículo
#              (as horas viram int).
#
# PARTE 4 · As filhas
#   Moto é um Veiculo que SUBSTITUI o valor(): 3.0 por hora.
#   Caminhao é um Veiculo com eixos. O __init__ recebe placa, modelo, eixos
#   e horas (horas = 1 como padrão):
#     se eixos for menor que 2, raise ValueError("caminhão tem pelo menos 2 eixos")
#     ANTES do super(); depois, super().__init__ e guarde os eixos.
#   valor()    ESTENDE o do pai: o valor do pai vezes os eixos.
#   __str__    ESTENDE o do pai:  CAM9Z87 Scania · 2h · R$ 36.00 · 3 eixos
#
# PARTE 5 · O ticket e o estacionamento
#   Ticket guarda numero e veiculo (o veículo chega pronto).
#     __str__  RETORNA:  #1 ABC1D23 Gol · 3h · R$ 18.00
#   Estacionamento: o __init__ recebe nome e vagas (vagas = 3 como padrão)
#   e começa com a lista self.tickets vazia.
#     entrar(veiculo)  se já não houver vaga, raise EstacionamentoLotadoError
#                      com o texto "Shopping Flamboyant lotado" (o nome dele +
#                      " lotado"). Se houver, CRIA o Ticket (o número é a
#                      quantidade de tickets + 1), guarda na lista e RETORNA.
#
# PARTE 6 · As contas
#   faturamento()  RETORNA a soma do valor() de todos os veículos dos tickets.
#   motos()        RETORNA quantos veículos dos tickets são Moto (isinstance).
#
# PARTE 7 · O seu estacionamento (escreva você, embaixo do teste)
#   Crie um Estacionamento com o nome de um lugar real de Goiás que você
#   conhece (shopping, faculdade, hospital, feira...) e vagas à sua escolha.
#   Crie 3 veículos SEUS, todos com modelos reais e a cor no modelo:
#     um Veiculo, por exemplo  Veiculo("PQR4S56", "Onix prata", 2)
#     uma Moto e um Caminhao (com os eixos que quiser)
#   Invente as placas no formato novo: 3 letras, 1 número, 1 letra, 2 números.
#   Coloque os 3 no estacionamento com entrar() e mostre com print
#   cada ticket e o faturamento().
#
# SE TRAVAR, REVEJA:
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   contador ............... aula 05, slide 21  https://poo.leoad.com.br/aulas/aula-05/#s21
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


# PARTE 1
class EstacionamentoLotadoError:
    pass  # falta o pai entre parênteses


class Veiculo:
    pass  # apague este pass quando escrever a classe

    # PARTE 2: as properties placa e horas (com o setter)

    # PARTE 3: valor, __str__, __repr__ e de_texto


# PARTE 4
class Moto(Veiculo):
    pass


class Caminhao(Veiculo):
    pass


# PARTE 5
class Ticket:
    pass


class Estacionamento:
    pass

    # PARTE 6: faturamento e motos


# ===== TESTE (não altere estas linhas) =====
# --- PARTES 1 a 3: o Veiculo ---
gol = Veiculo("ABC1D23", "Gol", 3)
uno = Veiculo("UNO2E34", "Uno")                      # horas fica 1
hb20 = Veiculo.de_texto("HBV5F67;HB20;2")

print(gol)                       # ABC1D23 Gol · 3h · R$ 18.00
print(repr(uno))                 # Veiculo('UNO2E34', 'Uno', 1)
print(hb20.valor())              # 12.0
print(Veiculo.total)             # 3

recusas = 0
for horas in [0, -2]:
    try:
        Veiculo("ERR0R00", "Teste", horas)
    except ValueError as erro:
        print("recusado:", erro)  # recusado: o mínimo é 1 hora
        recusas = recusas + 1
try:
    gol.horas = 0
except ValueError:
    recusas = recusas + 1
print(gol.horas, recusas)        # 3 3

# --- PARTE 4: as filhas ---
moto = Moto("MOT0A12", "CG 160", 4)
scania = Caminhao("CAM9Z87", "Scania", 3, 2)

print(moto)                      # MOT0A12 CG 160 · 4h · R$ 12.00
print(scania)                    # CAM9Z87 Scania · 2h · R$ 36.00 · 3 eixos
print(Veiculo.total)             # 5
try:
    Caminhao("ERR0R01", "Teste", 1)
except ValueError as erro:
    print("recusado:", erro)      # recusado: caminhão tem pelo menos 2 eixos
    recusas = recusas + 1
print(recusas)                   # 4
print(isinstance(scania, Veiculo), isinstance(gol, Caminhao))              # True False

# --- PARTES 5 e 6: o estacionamento ---
shopping = Estacionamento("Shopping Flamboyant")     # 3 vagas
print(shopping.entrar(gol))      # #1 ABC1D23 Gol · 3h · R$ 18.00
shopping.entrar(moto)
shopping.entrar(scania)
try:
    shopping.entrar(uno)
except EstacionamentoLotadoError as erro:
    print("barrado:", erro)       # barrado: Shopping Flamboyant lotado
print(len(shopping.tickets), shopping.faturamento(), shopping.motos())    # 3 66.0 1

print(f"chave: {Veiculo.total}-{gol.horas}-{recusas}-{shopping.faturamento()}-{shopping.motos()}-{len(str(scania))}-{isinstance(gol, Caminhao)}")


# ===== PARTE 7: o seu estacionamento (escreva aqui embaixo) =====

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex09.py.
# ============================================================
# SAÍDA:
