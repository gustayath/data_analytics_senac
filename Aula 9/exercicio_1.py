def calc_imc(peso, altura):
    imc = peso / altura **2
    
    print(f"{imc:.2f}")

    if imc > 40:
        print("Você esta com obesidade de grau III\n")
    elif imc <= 40 and imc >= 35:
        print("Você esta com obesidade de grau II\n")
    elif imc <= 34.9 and imc >= 30:
        print("Você esta com obesidade de grau I\n")
    elif imc <= 29.9 and imc >= 25:
        print("Você esta Acima do peso\n")
    elif imc <= 24.9 and imc >= 18.5:
        print("Você esta com peso normal\n")
    elif imc <= 18.4 and imc >= 17:
        print("Você esta abaixo do peso\n")
    else:
        print("Você esta muito abaixo do peso \n")
    return imc

controlador = 1

while controlador == 1:
    peso = float(input("Digite o seu peso ( USE PONTO, NÃO VIRGULA ): "))
    altura = float(input("Digite a sua altura ( USE PONTO, NÃO VIRGULA ): "))
    print("\n")
    try:    
        calc_imc(peso, altura)
    except ZeroDivisionError:
        print("\n============================================\nNão é possível realizar divisão por 0!\nDigite o peso e a altura correta!\n============================================\n")
    else:
        imc = calc_imc(peso, altura)
        print(f"Seu imc é: {imc}")
        print("Você deseja testar mais alguem? \nDigite 1 para sim e 0 para não")
        controlador = int(input(""))

print("Fim do programa")