def par_impar(numeros = 0):
    par = []
    impar = []
    for v in range(1, 21):
        numeros = int(input(f"{v} Número: "))
        if numeros % 2 == 0:
            par.append(numeros)
        else:
            impar.append(numeros)
    return f"Lista Ímpares: {impar}\nLista Pares: {par}"

print(par_impar())