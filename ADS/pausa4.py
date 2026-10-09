def media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    return soma / len(notas)

notas = [8, 6, 10]
print("Média: ", media(notas))
print("chave:", f"{len(notas)}-{media(notas)}")