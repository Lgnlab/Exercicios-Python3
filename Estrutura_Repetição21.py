def primo(numero = 0):
    numero = int(input('Informe um valor: '))
    cont = 0
    for p in range(1, numero + 1):
        if numero % p == 0:
            cont += 1
    if cont > 2 or numero == 1:
        return f'{numero} NÃO É PRIMO!'
    else:
        return f'{numero} É PRIMO!'


print(primo())