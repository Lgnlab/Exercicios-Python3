def pares_impares(valores = 0):
    lista = [[], []]
    cont = 1
    while cont <= 7:
        valores = int(input('Informe um valor: '))
        if valores % 2 == 0:
            lista[0].append(valores)
        else:
            lista[1].append(valores)
        cont += 1
    return f'Lista Ímpares: {lista[1]}\nLista Pares: {lista[0]}'


print(pares_impares())        