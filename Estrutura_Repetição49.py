def operando(limite = 0):
    limite = int(input("Quantos termos você quer ver(n)? "))
    cont = 1
    soma = 0
    denominador = 1
    while cont <= limite:
        termo = cont / denominador
        soma += termo
        if cont < limite:
            print(f"{cont}/{denominador}", end=' + ')
        else:
            print(f"{cont}/{denominador}")
        denominador += 2
        cont += 1
    return f"A soma da série é: {soma:.2f}"

print(operando())