def primos(numero = int):
    numero = int(input('Informe um valor: '))
    cont_parada = 1
    divisao = 0
    while cont_parada <= numero:
        if numero % cont_parada == 0:
            divisao += 1
        cont_parada += 1
    if divisao > 2 or numero == 0:
        return f"{numero} NÃO É PRIMO!"
    else:
        return f"{numero} É PRIMO!"

print(primos())