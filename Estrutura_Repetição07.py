def maior_numero(*numeros):
    maior = 0
    for c in range(1, 6):
        numeros = int(input(f'{c} Número: '))
        if c == 1:
            maior = numeros
        else:
            if numeros > maior:
                maior  = numeros
    return f"O maior número digitado: {maior}"


print(maior_numero())