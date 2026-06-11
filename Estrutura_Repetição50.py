def calculo(termos = 0):
    termos = int(input("Quantos termos você quer ver(n): "))
    soma = 0
    h = 1
    for cont in range(1, termos + 1):
        termo = h / cont
        soma += termo
        if cont < termos:
            print(f"{h}/{cont}", end=' + ')
        else:
            print(f"{h}/{cont}")
    return f"Soma da série: {soma:.2f}"

print(calculo())