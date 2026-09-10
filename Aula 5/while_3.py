contador = 0
elegivel = 0

while contador < 10:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        elegivel += 1
    contador += 1

print(f"Quantidade de pessoas elegíveis: {elegivel}")