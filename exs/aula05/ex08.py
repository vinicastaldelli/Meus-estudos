# Aula 05 · Exercício 08 (casa, desafio): o pedido completo da lanchonete
#
# Cliente: o __init__ recebe nome.
# Produto: o __init__ recebe nome e preco.
#   preco  @property e @preco.setter. O setter RECUSA preço negativo:
#              raise ValueError("preço não pode ser negativo")
#   de_texto(texto)  construtor alternativo, com @classmethod: recebe "Pastel;8"
#                    e RETORNA cls(nome, preco), com o preço convertido por float().
# ItemPedido: o __init__ recebe produto (um Produto) e quantidade.
#   subtotal()  RETORNA o preço do produto vezes a quantidade.
# Pedido:
#   atributos de CLASSE: taxa_entrega = 6 e total_pedidos = 0.
#   o __init__ recebe cliente (um Cliente JÁ CRIADO: associação), cria
#     self.itens como lista vazia e soma 1 em Pedido.total_pedidos.
#   adicionar(produto, quantidade)  CRIA o ItemPedido ali dentro (composição).
#   subtotal()  RETORNA a soma dos subtotais dos itens, usando um for.
#   total()     RETORNA o subtotal mais a taxa de entrega. Com subtotal de 50
#               ou mais, a entrega é grátis.
#   __str__     retorna, por exemplo: Pedido de Ana: 2 itens, total R$ 28.50
#               (o total sempre com 2 casas decimais: :.2f)
#
# Exemplos:
#   ana = Cliente("Ana")
#   pastel = Produto.de_texto("Pastel;8")
#   caldo = Produto.de_texto("Caldo de cana;6.5")
#   Pedido(ana) com 2 pastéis e 1 caldo: subtotal() 22.5, total() 28.5,
#   e o print do pedido mostra Pedido de Ana: 2 itens, total R$ 28.50
#   Pedido(ana) com 7 pastéis: total() 56.0 (entrega grátis).
#   Depois de Pedido.taxa_entrega = 8, o primeiro pedido passa a ter total() 30.5.
#   Depois desses dois pedidos, Pedido.total_pedidos vale 2.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   associação ............. aula 05, slide 39  https://poo.leoad.com.br/aulas/aula-05/#s39
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
