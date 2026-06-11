def calculo(termos = 0):
    termos = int(input("Termos(n): "))
    soma = 0
    divisor = 1
    for cont in range(1, termos + 1):
        termo = cont / divisor
        soma += termo
        if cont < termos:
            print(f"{cont}/{divisor}", end=' + ')
        else:
            print(f"{cont}/{divisor}")
        divisor += 2
    return f"Soma da série: {soma:.2f}"

print(calculo())