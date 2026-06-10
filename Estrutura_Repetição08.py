def numero(*numeros):
    cont = 1
    soma = 0
    while cont <= 5:
        numeros = int(input(f'{cont} Número: '))
        soma += numeros
        cont += 1
    return f"Soma dos números digitados: {soma}\nMédia: {soma / 5:.1f}"


print(numero())