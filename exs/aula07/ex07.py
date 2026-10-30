# Aula 07 · Exercício 07 (casa, opcional): avisos com duck typing
#
# Crie três classes SEM herança, todas com o método enviar(msg), que RETORNA um texto:
#   Email(endereco)   enviar("Intervalo às 20h10")  retorna  E-mail para ana@email.com: Intervalo às 20h10
#   Sms(numero)       enviar("Intervalo às 20h10")  retorna  SMS para 62 99999-0000: Intervalo às 20h10
#                     numero com @property e @numero.setter. O setter RECUSA
#                     número com menos de 8 caracteres (use len):
#                         raise ValueError("número inválido")
#                     O __init__ faz self.numero = numero: o setter roda na criação.
#   Telao()           enviar("Intervalo às 20h10")  retorna  TELÃO: Intervalo às 20h10
# Crie a função avisar_todos(canais, msg), que RETORNA uma lista com o texto de
# cada canal, na ordem (comece com textos = [] e use append). Sem nenhum if.
#
# Depois crie a classe Pombo com o método mandar(msg) e coloque um Pombo() na
# lista de canais. Rode, leia o erro e escreva num comentário o que ele quer dizer.
# Por fim, conserte a classe Pombo (sem mexer na função) para ela entrar no aviso:
#   Pombo()   enviar("Intervalo às 20h10")  retorna  Pombo levou: Intervalo às 20h10
# Na SAÍDA, cole a saída final, já com o Pombo consertado.
#
# Teste você mesmo: no fim do arquivo, crie os canais e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que Sms("190") é recusado.
#
# SE TRAVAR, REVEJA:
#   duck typing ............ aula 07, slide 13  https://poo.leoad.com.br/aulas/aula-07/#s13
#   assinatura ............. aula 07, slide 19  https://poo.leoad.com.br/aulas/aula-07/#s19
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
