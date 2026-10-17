digitados = ["18", "vinte", "25", ""]    # o que a pessoa digitou

soma = 0
for texto in digitados:
    try:
        idade = int(texto)
        soma = soma + idade
        print("ok:", idade)
    except ValueError:
        print("não é número:", repr(texto))

print("Soma das idades:", soma)

# ok: 18
# não é número: 'vinte'
# ok: 25
# não é número: ''
# Soma das idades: 43