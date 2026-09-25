import math as mt

mt.ceil(4.2)    # 5  (arredonda para cima)
mt.floor(4.8)   # 4  (arredonda para baixo)
mt.trunc(4.9)   # 4  (remove a parte decimal)
mt.fabs(-7)     # 7.0 (valor absoluto como float)
mt.sqrt(16)     # 4.0  (raiz quadrada)
mt.pow(2, 10)   # 1024.0 (potência), pow(base, expoente)
mt.gcd(12, 18)      # 6  (máximo divisor comum)
mt.pi      # 3.141592653589793 valor de PI

numero = float(input("Digite um número: "))

print(f"A raiz quadrada é: {mt.sqrt(numero)}")
print(f"O número elevado ao cubo é: {mt.pow(numero, 3)}")