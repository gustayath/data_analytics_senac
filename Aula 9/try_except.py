def somar_numeros(num1, num2):
    soma = num1 + num2
    return soma

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
except ValueError:
    print("ERRO! valor inválido!")
else:
    print(f"A soma dos dois números são: {somar_numeros(numero1, numero2)}")