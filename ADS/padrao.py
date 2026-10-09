def saudacao(nome, periodo="dia"):
    return f"Bom {periodo}, {nome}!"

print(saudacao("Ana"))              # Bom dia, Ana!
print(saudacao("Bruno", "fim de semana"))   # Bom fim de semana, Bruno!
print(saudacao("Carla", periodo="trabalho"))  # Bom trabalho, Carla!

print(saudacao())
# TypeError: saudacao() missing 1 required positional argument: 'nome'