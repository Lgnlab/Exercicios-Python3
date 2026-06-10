def primo(numero = 0):
    numero = int(input('Informe um valor: '))
    cont = 0
    lista = []
    for p in range(1, numero + 1):
        if numero % p == 0:
            lista.append(p)
            cont += 1
    if cont > 2 or numero == 1:
        return f'{numero} NÃO É PRIMO!\nNúmeros divisiveis: {lista}'
    else:
        return f'{numero} É PRIMO!'


print(primo())