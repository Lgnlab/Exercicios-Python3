def numeros_impares():
    cont = 1
    while cont <= 50:
        if cont % 2 != 0:
            print(cont, end=' ')
        cont += 1

numeros_impares()