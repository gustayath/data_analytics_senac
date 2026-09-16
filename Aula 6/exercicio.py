num = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    num.append(numero)

maior = max(num)
menor = min(num)
soma = sum(num)

print("\nLista:", num)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Soma:", soma)

tupla = tuple(num)

print("Tupla final:", tupla)