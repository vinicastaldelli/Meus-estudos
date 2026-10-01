class Equipamento:
    def __init__(self, nome, patrimonio, setor = "Não informado"):
        self.nome = nome
        self.patrimonio = patrimonio
        self.setor = setor
        self.disponivel = True
        if not nome.strip():
            raise ValueError("Nome obrigatório")
        if not patrimonio.startswith("PAT-"):
            raise ValueError(...)
        
    def exibir_dados(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.patrimonio} - {self.nome} - {self.setor} - {status}"

notebook = Equipamento("Notebook Dell", "PAT-001")
projetor = Equipamento("Projetor Epson", "PAT-002")
notebook2 = Equipamento("Mack book Air", "MAC-003")

print(notebook.exibir_dados())
print(projetor.exibir_dados())
print(notebook2.exibir_dados())
