turma = []

for i in range(5):
    turma.append({"nome": input("\nDigite o nome do aluno: ")})
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    turma[i].update({"media": media})
    if turma[i]["media"] >= 7:
        turma[i].update({"status": "Aprovado"})
    elif turma[i]["media"] >= 5 and turma[i]["media"] <= 6.9:
        turma[i].update({"status": "Recuperação"})
    else:
        turma[i].update({"status": "Reprovado"})

for i in range(len(turma)):
    print(f"\nAluno: {turma[i]['nome']}")
    print(f"Média: {turma[i]['media']:.2f}")
    print(f"Situação: {turma[i]['status']}")
