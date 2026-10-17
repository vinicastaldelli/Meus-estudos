def dividir_conta(total, texto_pessoas):
    pessoas = int(texto_pessoas)    # pode dar ValueError
    return total / pessoas          # pode dar ZeroDivisionError

for texto in ["4", "quatro", "0"]:
    try:
        print("cada um paga:", dividir_conta(120, texto))
    except ValueError:
        print("escreva o número com algarismos")
    except ZeroDivisionError:
        print("a conta precisa de pelo menos 1 pessoa")

# cada um paga: 30.0
# escreva o número com algarismos
# a conta precisa de pelo menos 1 pessoa