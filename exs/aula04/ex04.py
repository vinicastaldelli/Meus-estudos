# Aula 04 · Exercício 04 (casa, OBRIGATÓRIO): o cofrinho
#
# Crie a classe Cofrinho. O __init__ recebe dono, e todo cofrinho nasce com
# saldo 0.
# saldo             @property SÓ DE LEITURA (sem setter): RETORNA self._saldo.
#                   Por isso o __init__ grava direto: self._saldo = 0, e os
#                   métodos também mexem em self._saldo.
# depositar(valor)  se o valor for 0 ou menos, LEVANTE
#                   ValueError("depósito precisa ser maior que zero");
#                   senão, soma o valor ao saldo.
# retirar(valor)    se o valor for 0 ou menos, LEVANTE
#                   ValueError("retirada precisa ser maior que zero");
#                   se o valor for maior que o saldo, LEVANTE
#                   ValueError("saldo insuficiente");
#                   senão, tira do saldo e RETORNA o saldo que sobrou.
# __str__           RETORNA, por exemplo:  Cofrinho da Ana: R$ 30.00
# Nada de print nem de return None no lugar do raise.
#
# Teste você mesmo: no fim do arquivo, crie um cofrinho e faça pelo menos
# 4 operações, cada uma dentro de um try com except ValueError as erro,
# mostrando com print o resultado ou a mensagem do erro. Inclua um depósito
# recusado e uma retirada recusada. Por exemplo:
#   depositou 50, saldo 50
#   recusado: depósito precisa ser maior que zero
#   retirou 20, sobrou 30
#   recusado: saldo insuficiente
# No fim, mostre o cofrinho com print(cofrinho), que usa o seu __str__.

class Cofrinho:
    def __init__(self, dono):
        self._dono = dono
        self._saldo = 0
    @property
    def dono(self):
        return self._dono
    @property
    def saldo(self):
        return self._saldo
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("depósito precisa ser maior que zero")
        self._saldo += valor
    def retirar(self, valor):
        if valor <= 0:
            raise ValueError("retirada precisa ser maior que zero")
        elif valor > self._saldo:
            raise ValueError("saldo insuficiente")
        self._saldo -= valor
        return self._saldo
    def __str__(self):
        return f"Cofrinho de {self._dono}: R$ {self._saldo:.2f}"

cofrinho = Cofrinho("Ana")

try:
    cofrinho.depositar(50)
    print("depositou 50, saldo 50")
except ValueError as erro:
    print(f"recusado: {erro}")

try:
    cofrinho.depositar(0)
except ValueError as erro:
    print(f"recusado: {erro}")

try:
    sobra = cofrinho.retirar(20)
    print(f"retirou 20, sobrou {sobra}")
except ValueError as erro:
    print(f"recusado: {erro}")

try:
    cofrinho.retirar(999)
except ValueError as erro:
    print(f"recusado: {erro}")

try:
    sobra = cofrinho.retirar(10)
    print(f"retirou 10, sobrou {sobra}")
except ValueError as erro:
    print(f"recusado: {erro}")

print(cofrinho)

# SE TRAVAR, REVEJA:
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   except ... as erro ..... aula 04, slide 15  https://poo.leoad.com.br/aulas/aula-04/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# depositou 50, saldo 50
# recusado: depósito precisa ser maior que zero
# retirou 20, sobrou 30
# recusado: saldo insuficiente
# retirou 10, sobrou 20
# Cofrinho de Ana: R$ 20.00