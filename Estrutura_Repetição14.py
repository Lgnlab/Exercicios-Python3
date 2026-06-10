def quantidade_ip(*numeros):
    cont_i = cont_p = 0
    for cont in range(1, 11):
        numeros = int(input(f'{cont} Número: '))
        if numeros % 2 == 0:
            cont_p += 1
        else:
            cont_i += 1
    return f"Impares: {cont_i}\nPares: {cont_p}"


print(quantidade_ip())