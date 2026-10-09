frutas = ["banana", "maçã", "uva"]

print(frutas)           # ['banana', 'maçã', 'uva']
print(frutas[0])        # banana   (o primeiro é o índice 0)
print(frutas[2])        # uva
print(frutas[-1])       # uva      (-1 é sempre o último)
print(len(frutas))      # 3

frutas.append("manga")  # coloca no fim
print(frutas)           # ['banana', 'maçã', 'uva', 'manga']
print(len(frutas))      # 4

frutas[1] = "pera"      # troca o item do índice 1
print(frutas)           # ['banana', 'pera', 'uva', 'manga']

print(frutas[4])        # IndexError: list index out of range