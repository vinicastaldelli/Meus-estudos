with open("atendimento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Bruno\n")

with open("atendimento.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Caio\n")

with open("atendimento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Duda\n")

with open("atendimento.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Edu")
    arquivo.write("Fabi\n")

nomes = []
with open("atendimento.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nomes.append(linha.strip())

print(nomes)         # ?
print(len(nomes))    # ?
print(f"chave: {len(nomes)}-{nomes[0]}-{nomes[-1]}")    # ?