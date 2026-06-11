def numero_invertido(numero = 0):
    numero = int(input("Informe um valor: "))
    texto = str(numero)
    inverte = texto[::-1]
    return f"{numero} => {inverte}"

print(numero_invertido())