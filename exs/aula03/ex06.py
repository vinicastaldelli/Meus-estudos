# Aula 03 · Exercício 06 (casa, opcional): a senha do Usuario
#
# Classe Usuario. O __init__ recebe login e senha (a senha pelo setter).
# login     @property só de leitura.
# senha     @property que RETORNA sempre "********": a senha de verdade,
#           guardada em self._senha, nunca sai do objeto.
#           @senha.setter: RECUSA senha com menos de 8 caracteres (use len) com
#           raise ValueError("A senha precisa ter 8 caracteres ou mais")
# verificar(tentativa)   RETORNA True se a tentativa for igual à senha
#                        guardada, senão False.
# __repr__  retorna, por exemplo: Usuario('ana.silva')
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Troque a senha de um deles e verifique de novo.
# Se quiser ver a recusa, deixe essa tentativa como ÚLTIMA linha: o programa
# para no seu ValueError e o que vem depois não roda.

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self._senha = senha

    @property
    def login(self):
        return self._login

    @property
    def senha(self):
        return "********"

    @senha.setter
    def senha(self, valor):
        if len(valor) < 8:
            raise ValueError("A senha deve ter 8 caracteres ou mais")
        self._senha = valor

    def verificar(self, tentativa):
        if tentativa == self._senha:
            return True
        return False

    def __repr__(self):
        return f"Usuario('{self.login}')"

u1 = Usuario("ana.silva", "minhasenha")
u2 = Usuario("joao", "12345678")
print(u1.login)
print(u1.senha)
print(u1.verificar("minhasenha"))
print(u1.verificar("outra"))
print(repr(u1))
u2.senha = "novaSenha9"
print(u2.senha)
print(u2.verificar("novaSenha9"))
print(u2.verificar("12345678"))
u1.senha = "curta"

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# Traceback (most recent call last):
#   File "c:\Meus-estudos\exs\aula03\ex06.py", line 45, in <module>
#     u1 = Usuario("ana.silva", "minhasenha")
#   File "c:\Meus-estudos\exs\aula03\ex06.py", line 20, in __init__
#     self.login = login
#     ^^^^^^^^^^
# AttributeError: property 'login' of 'Usuario' object has no setter