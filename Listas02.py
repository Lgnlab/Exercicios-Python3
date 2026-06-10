def valores_numericos(numeros = 0):
    valores = []
    while True:
        numeros = int(input('Informe um valor(digite 999 para parar): '))
        if numeros == 999:
            break
        else:
            if numeros not in valores:
                valores.append(numeros)
            else:
                print('\033[31mValor repetido!Tente novamente.\033[m')
    valores.sort()
    return valores


print(valores_numericos())