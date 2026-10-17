try:
    idade = int("vinte")
except ValueError as erro:
    print("Mensagem:", erro)    # Mensagem: invalid literal for int() with base 10: 'vinte'
    print("Tipo:", type(erro))  # Tipo: <class 'ValueError'>

problema = ValueError("desconto maior que 100%")    # só cria o objeto: nada para
print(problema)          # desconto maior que 100%
print(type(problema))    # <class 'ValueError'>