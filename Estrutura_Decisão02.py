def positivo_negativo(numero = 0):
    numero = int(input('Informe um valor: '))
    if numero < 0:
        return f'O {numero} é NEGATIVO!'
    else:
        return f'O {numero} é POSITIVO!'
    

print(positivo_negativo())