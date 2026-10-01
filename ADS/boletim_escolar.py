alunos = []

print("-" * 50)
print("Boletim do Aluno")
print("-" * 50)

while len(alunos) < 50:
    print(f"\nAluno {len(alunos) + 1} de 50")

    nome = input("Nome: ")
    email = input("E-mail: ")
    matricula = input("Matrícula: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    media = (nota1 + nota2 + nota3) / 3
    
    alunos.append({"nome": nome, "matricula": matricula, "email": email, "media": media})

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

alunos.append({
    "nome": nome,
    "email": email,
    "matricula": matricula,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "media": media,
    "situacao": situacao
})

print(f"\nTotal de alunos: {len(alunos)}\n")

print(f"{'MATRÍCULA':<12}{'NOME':<22}{'E-MAIL':<25}{'NOTA 1':>6}{'NOTA 2':>6}{'NOTA 3':>6}{'MÉDIA':>8}{'SITUAÇÃO':>15}")
print("-" * 100)

for aluno in alunos:
    print(
        f"{aluno['matricula']:<12}"
        f"{aluno['nome']:<22}"
        f"{aluno['email']:<25}"
        f"{aluno['nota1']:>6.2f}"
        f"{aluno['nota2']:>6.2f}"
        f"{aluno['nota3']:>6.2f}"
        f"{aluno['media']:>8.2f}"
        f"{aluno['situacao']:>15}"
    )

aprovados = 0
recuperacao = 0
reprovados = 0

for aluno in alunos:
    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    elif aluno["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print("-" * 100)
print(f"Totais -> Aprovados: {aprovados} | Em Recuperação: {recuperacao} | Reprovados: {reprovados}")
