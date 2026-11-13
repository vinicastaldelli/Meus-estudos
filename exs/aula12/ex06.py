# Aula 12 · Exercício 06 (casa, opcional): o diário de treinos
#
# Comece o arquivo com:  from pathlib import Path
#
# Treino: o __init__ recebe atividade e minutos e guarda os dois.
#   para_linha() e de_linha(linha), como na aula (minutos volta como int).
#
# anotar(treino, caminho): ACRESCENTA o treino no fim do arquivo (modo "a").
# carregar(caminho): RETORNA a lista de Treino, pulando as linhas em branco.
# minutos_por_atividade(treinos): RETORNA um dicionário com o total de minutos
#   de cada atividade. Para somar, use .get(atividade, 0).
#
# Exemplo: anote Treino("corrida", 30), Treino("natação", 45),
# Treino("corrida", 40) e Treino("bike", 60) em treinos.txt
# (Path(__file__).parent / "treinos.txt"). Depois da 1ª vez que você rodar,
# minutos_por_atividade(carregar(...)) mostra:
#   {'corrida': 70, 'natação': 45, 'bike': 60}
# Rode de novo: os treinos da 1ª vez continuam no arquivo, e os totais dobram.
#
# Teste você mesmo: no fim do arquivo, anote, carregue e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   modo a ................. aula 11, slide 10  https://poo.leoad.com.br/aulas/aula-11/#s10
#   de_linha e para_linha .. aula 12, slide 6  https://poo.leoad.com.br/aulas/aula-12/#s6
#   linha em branco ........ aula 12, slide 12  https://poo.leoad.com.br/aulas/aula-12/#s12
#   dicionário ............. aula 10, slide 33  https://poo.leoad.com.br/aulas/aula-10/#s33
#   [ ] × .get() ........... aula 10, slide 34  https://poo.leoad.com.br/aulas/aula-10/#s34

from pathlib import Path

class Treino:
    def __init__(self, atividade, minutos):
        self.atividade = atividade
        self.minutos = minutos

    def para_linha(self):
        return f"{self.atividade};{self.minutos}"

    @classmethod
    def de_linha(cls, linha):
        atividade, minutos = linha.strip().split(";")
        return cls(atividade, int(minutos))

def Anotar(treino, caminho):
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(treino.para_linha() + "\n")

def carregar(caminho):
    treino = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip():
                    treino.append(Treino.de_linha(linha))
    except FileNotFoundError:
        return []
    return treino

def minutos_por_atividade(treinos):
    totais = {}
    for treino in treinos:
        atividade = treino.atividade
        totais[atividade] = totais.get(atividade, 0) + treino.minutos
    return totais

caminho = Path(__file__).parent / "treinos.txt"

novos_treinos = [
    Treino("corrida", 30),
    Treino("natação", 45),
    Treino("corrida", 40),
    Treino("bike", 60),
]

for treino in novos_treinos:
    Anotar(treino, caminho)

treinos_carregados = carregar(caminho)
print(minutos_por_atividade(treinos_carregados))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# {'corrida': 70, 'natação': 45, 'bike': 60}