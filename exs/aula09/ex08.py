# Aula 09 · Exercício 08 (casa, desafio): o pet shop
#
# Escreva todas as classes do diagrama, e só elas:
#   https://poo.leoad.com.br/images/aula-09/ex08-petshop.svg
# Leia cada linha antes de escrever:
#   PetShop ◆ Cliente   o pet shop CRIA o cliente em cadastrar(nome),
#                       guarda na lista e RETORNA o cliente criado.
#   Cliente e Pet       linha simples: o cliente RECEBE pets prontos em adicionar(pet).
#   Pet △ Cachorro, Gato   Pet é abstrata; banho() e especie() são abstratos.
#   Exception △ ClienteNaoEncontradoError   uma exceção própria.
#
# banho()   Gato: 50. Cachorro: 60 se o porte for "pequeno", 90 se não.
# Cliente.total_banhos()   RETORNA a soma dos banhos dos pets dele.
# PetShop.buscar(nome)     RETORNA o cliente com esse nome. Se não houver,
#                          raise ClienteNaoEncontradoError(nome).
# especie()                RETORNA "cachorro" ou "gato".
# Pet.__str__              concreto, no pai: Rex (cachorro)  ou  Mimi (gato)
#                          (use self.especie() no texto).
#
# Teste você mesmo: cadastre dois clientes, dê pets a eles, mostre os
# totais e provoque a busca que não encontra, dentro de um try/except.
#
# SE TRAVAR, REVEJA:
#   linhas do diagrama ..... aula 09, slide 15  https://poo.leoad.com.br/aulas/aula-09/#s15
#   o triângulo ............ aula 09, slide 21  https://poo.leoad.com.br/aulas/aula-09/#s21
#   «abstract» ............. aula 09, slide 27  https://poo.leoad.com.br/aulas/aula-09/#s27
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34

from abc import ABC, abstractmethod


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
