registro = []

def acender_luz():
    registro.append("luz")

def tocar_musica():
    registro.append("musica")

class Campainha:
    def __init__(self):
        self.acoes = []

    def inscrever(self, funcao):
        self.acoes.append(funcao)

    def tocar(self):
        for acao in self.acoes:
            acao()

c = Campainha()
c.inscrever(acender_luz)
c.inscrever(tocar_musica)
c.tocar()
c.tocar()

print(registro)    # ['luz', 'musica', 'luz', 'musica']
print(f"chave: {len(registro)}-{registro[1]}-{len(c.acoes)}")