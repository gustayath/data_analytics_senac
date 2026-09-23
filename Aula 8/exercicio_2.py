total_peso = float(input("Digite o peso total dos peixes pescados neste dia (somente o peso): "))

def calc_multa(valor):
    limite = 100
    multa = 4.00
    if total_peso > limite:
        excesso = total_peso - limite
        multa = excesso * multa
        return multa
    else:
        return 0

multa_peso = calc_multa(total_peso)

if multa_peso != 0:
    print(f"Multa de R$ {multa_peso:.2f}!")
else:
    print("Valor não excedeu limite e não gerou multa.")