linha = "Ana;1000"
partes = linha.split(";")    # corta o texto em cada ;

print(partes)          # ['Ana', '1000']
print(partes[0])       # Ana
print(partes[1])       # 1000
print(len(partes))     # 2

saldo = float(partes[1])     # float() faz como o int(), mas aceita número com ponto
print(saldo + 1)       # 1001.0
print("Bia;200;sim".split(";"))    # ['Bia', '200', 'sim']

print(partes[1] + 1)   # TypeError: can only concatenate str (not "int") to str