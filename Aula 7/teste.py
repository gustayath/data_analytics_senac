def soma_pares(numeros):
    soma = sum(numeros)
    print(f"O resultado da soma foi: {soma}")


for i in range(3):
    numeros = []

    for j in range(3):
        num = int(input("Digite um número par: "))
        numeros.append(num)

    soma_pares(numeros)