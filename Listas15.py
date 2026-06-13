def operacoes(numero = 0):
    import math
    lista = []
    for cont in range(1, 6):
        numeros = int(input(f"{cont} Número: "))
        lista.append(numeros)
    return f"Lista completa: {lista}\nSoma: {sum(lista)}\nMultiplicação: {math.prod(lista)}"

print(operacoes())