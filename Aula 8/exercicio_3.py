def calcular_imc(peso, altura):
    return peso / (altura ** 2)


for i in range(5):
    print(f"\nPessoa {i + 1}")

    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = calcular_imc(peso, altura)

    print(f"IMC: {imc:.2f}")

    if imc <= 16.9:
        print("Muito abaixo do peso! ")
    elif imc <= 18.4:
        print("Abaixo do peso! ")
    elif imc <= 24.9:
        print("Peso normal! ")
    elif imc <= 30:
        print("Acima do peso! ")
    elif imc <= 34.9:
        print("Obesidade grau 1! ")
    elif imc <= 40:
        print("Obesidade grau 2! ")
    else:
        print("Obesidade grau 3")