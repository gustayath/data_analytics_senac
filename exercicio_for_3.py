palavra = input("Digite uma palavra: ")
vezes = 0
for letra in palavra:
    print(letra)
    if letra == 'a':
        vezes = vezes + 1
print(f"A letra 'A' se repetiu: {vezes}")