# Inicialização da lista de alunos
alunos = []

print("=== CADASTRO DE ALUNOS (Limite: 50) ===")
print("Para fins de teste, você pode interromper antes ou rodar até o fim.")
print("-" * 50)

# Loop controlado por len(alunos) conforme a estratégia sugerida
while len(alunos) < 50:
    print(f"\nCadastrando aluno {len(alunos) + 1} de 50:")
    
    # Leitura dos dados obrigatórios
    nome = input("Nome completo: ").strip()
    # Permite parar o preenchimento mais cedo para testes rápidos
    if nome.lower() == 'sair': 
        break
        
    email = input("E-mail: ").strip()
    matricula = input("Matrícula: ").strip()
    
    # Leitura e validação das notas
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
    except ValueError:
        print("Erro: Digite valores numéricos válidos para as notas. Tente reiniciar o cadastro deste aluno.")
        continue

    # Calcular a média aritmética
    media = (nota1 + nota2 + nota3) / 3

    # Regras de classificação da situação
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Criando o dicionário do aluno para não sobrescrever registros
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "email": email,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    # Adicionando o aluno à lista
    alunos.append(aluno)

# --- EXIBIÇÃO DOS RESULTADOS (TABELA OBRIGATÓRIA) ---
print("\n" + "="*95)
print(f"{'Matrícula':<12} | {'Nome':<20} | {'E-mail':<25} | {'N1':<5} | {'N2':<5} | {'N3':<5} | {'Média':<6} | {'Situação'}")
print("="*95)

# Contadores para os totais por situação
total_aprovados = 0
total_recuperacao = 0
total_reprovados = 0

for a in Alunos:
    # Exibição formatada com f-strings mantendo as colunas alinhadas
    print(f"{a['matricula']:<12} | {a['nome']:<20} | {a['email']:<25} | {a['nota1']:<5.1f} | {a['nota2']:<5.1f} | {a['nota3']:<5.1f} | {a['media']:<6.1f} | {a['situacao']}")
    
    # Contagem para o relatório final
    if a['situacao'] == "Aprovado":
        total_aprovados += 1
    elif a['situacao'] == "Recuperação":
        total_recuperacao += 1
    elif a['situacao'] == "Reprovado":
        total_reprovados += 1

print("="*95)
0
# --- EXIBIR TOTAIS POR SITUAÇÃO ---
print(f"Total de alunos cadastrados: {len(alunos)}")
print(f"Alunos Aprovados: {total_aprovados}")
print(f"Alunos em Recuperação: {total_recuperacao}")
print(f"Alunos Reprovados: {total_reprovados}")
print("="*95)
