import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "tarefas.json"

class Tarefa:
    def __init__(self, titulo, feita):
        self.titulo = titulo
        self.feita = feita

    def para_dict(self):
        return {"titulo": self.titulo, "feita": self.feita}

    @classmethod
    def de_dict(cls, dados):
        return cls(dados["titulo"], dados["feita"])

tarefas = [Tarefa("Estudar", True), Tarefa("Lavar louça", False), Tarefa("Treinar", True)]

dados = []
for t in tarefas:
    dados.append(t.para_dict())
with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    lidas = json.load(arquivo)

feitas = 0
for item in lidas:
    tarefa = Tarefa.de_dict(item)
    if tarefa.feita:
        feitas = feitas + 1

print(lidas[1])    # {'titulo': 'Lavar louça', 'feita': False}
print(f"chave: {len(lidas)}-{feitas}-{Tarefa.de_dict(lidas[2]).titulo}")