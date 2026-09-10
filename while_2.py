soma = 0

while True:
    num = int(input("Digite um número: "))
    soma = soma + num

    if num == 0:
        break

print(f"O resultado da soma foi: {soma}")
