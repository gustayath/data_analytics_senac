funcionarios = []

for i in range(5):
    funcionarios.append({"idade": int(input("Digite a idade do candidato: "))})
    if funcionarios[i]["idade"] >= 18:
        funcionarios[i].update({'nome': input("Digite o seu nome: ")})
        funcionarios[i].update({'nascimento': input("Digite a data de nascimento do candidato: ")})
        funcionarios[i].update({'telefone': input("Digite o telefone do candidato: ")})
        funcionarios[i].update({'email': input("Digite o email do funcionario: ")})
        funcionarios[i].update({'Formação': input("Digite a formação do candidato: ")})
        print("\n")
    else:
        print("Candidato menor de idade, não aprovado para contrato. \n")

print("Candidatos: \n")

for i in range(len(funcionarios)):
    if 'nome' in funcionarios[i]:
        print(f"Nome do candidato: {funcionarios[i]}['nome']")
        print(f"Data de nascimento do candidato: {funcionarios[i]} ['nascimento']")
        print(f"Telefone do candidato: {funcionarios[i]} ['telefone']")
        print(f"Email do candidato: {funcionarios[i]} ['email']")
        print(f"Formação do candidato: {funcionarios[i]} ['formação']")
        print("\n")