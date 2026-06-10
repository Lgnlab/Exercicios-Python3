def lista_ordenada():
    valores = []
    for c in range(0, 5):
        numeros = (int(input(f'{c} Número: ')))
        if c == 0 or numeros > valores[-1]:
            valores.append(numeros)
        else:
            pos = 0
            while pos < len(valores):
                if numeros <= valores[pos]:
                    valores.insert(pos, numeros)
                    break
                pos += 1
    return valores


print(lista_ordenada())