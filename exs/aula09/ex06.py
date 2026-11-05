# Aula 09 · Exercício 06 (casa, opcional): o streaming
#
# Escreva as 3 classes do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex06-streaming.svg
# A Serie CRIA os próprios episódios (losango cheio). O Usuario RECEBE
# séries prontas (linha simples): várias pessoas assistem à mesma série.
#
# Serie.novo_episodio(titulo, minutos)  cria o Episodio e guarda na lista.
# Serie.duracao()                       RETORNA a soma dos minutos.
# Usuario.assistir(serie)               guarda a série recebida.
# Usuario.minutos_assistidos()          RETORNA a soma da duracao() das séries.
#
# Mostre também que duas pessoas assistindo à MESMA série guardam o mesmo
# objeto: compare com == as séries das duas listas.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print.
#
# SE TRAVAR, REVEJA:
#   linhas do diagrama ..... aula 09, slide 15  https://poo.leoad.com.br/aulas/aula-09/#s15
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42

class Episodio:
    def __init__(self, titulo, minutos):
        self.titulo = titulo
        self.minutos = minutos

class Serie:
    def __init__(self, titulo):
        self.titulo = titulo
        self.episodios = []

    def novo_episodio(self, titulo, minutos):
        episodio = Episodio(titulo, minutos)
        self.episodios.append(episodio)

    def duracao(self):
        soma = 0
        for episodio in self.episodios:
            soma += episodio.minutos
        return soma

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.series = []

    def assistir(self, serie):
        self.series.append(serie)

    def minutos_assistidos(self):
        soma = 0
        for serie in self.series:
            soma += serie.duracao()
        return soma
    
serie = Serie("Aventura no espaço")
serie.novo_episodio("A chegada", 40)
serie.novo_episodio("A descoberta", 35)

ana = Usuario("Ana")
bia = Usuario("Bia")
ana.assistir(serie)
bia.assistir(serie)

print("Duração da série:", serie.duracao())
print("Minutos assistidos por Ana:", ana.minutos_assistidos())
print("Minutos assistidos por Bia:", bia.minutos_assistidos())
print("É a mesma série?", ana.series[0] == bia.series[0])

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# Duração da série: 75
# Minutos assistidos por Ana: 75
# Minutos assistidos por Bia: 75
# É a mesma série? True