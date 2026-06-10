def pares_impares(numeros= 0):
    lista_inicial = []
    lista_impares = []
    lista_pares = []
    while True:
        numeros = int(input('Adicione um valor na lista: '))
        lista_inicial.append(numeros)
        sair = str(input('Quer continuar[S/N]?')).upper().strip()[0]
        if sair == 'N':
            break
    for l in lista_inicial:
        if l % 2 == 0:
            lista_pares.append(l)
        else:
            lista_impares.append(l)
    return f'Lista Ímpares: {lista_impares}\nLista Pares: {lista_pares}'


print(pares_impares())