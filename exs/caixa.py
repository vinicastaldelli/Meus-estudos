class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("saldo insuficiente")
        self.saldo = self.saldo - valor

def sacar_no_caixa(conta, valor):
    try:
        conta.sacar(valor)                      # pode recusar
    except ValueError as erro:
        print("Saque recusado:", erro)
    else:
        print("Retire as notas: R$", valor)     # só se o saque deu certo
    finally:
        print("Retire o cartão")                # sempre

conta = ContaBancaria("Ana", 100)
sacar_no_caixa(conta, "cem")   # caminho 3: um erro que ninguém previu
print("próximo cliente")       # não roda

# Retire o cartão
# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\caixa.py", line 22, in <module>
#     sacar_no_caixa(conta, "cem")   # caminho 3: um erro que ninguém previu
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\caixa.py", line 13, in sacar_no_caixa
#     conta.sacar(valor)                      # pode recusar
#     ~~~~~~~~~~~^^^^^^^
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\aula-04\caixa.py", line 7, in sacar
#     if valor > self.saldo:
#        ^^^^^^^^^^^^^^^^^^
# TypeError: '>' not supported between instances of 'str' and 'int'