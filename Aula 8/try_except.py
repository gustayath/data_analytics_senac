try:
     numero = int(input("Digite um número: "))
except(ValueError):
    print("Erro; número não digitado! ")
else:
    print(f"Você digitou o número: {numero}")
finally:
    print("Fim do programa")