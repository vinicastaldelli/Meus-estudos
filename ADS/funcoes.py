def area_retangulo(base, altura):
    return base * altura

a = area_retangulo(3, 4)
print(a)                          # 12
print(area_retangulo(10, 2))      # 20
print(area_retangulo(3, 4) + 1)   # 13   (o valor devolvido entra na conta)

def media(numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma / len(numeros)

print(media([8, 6, 10]))          # 8.0