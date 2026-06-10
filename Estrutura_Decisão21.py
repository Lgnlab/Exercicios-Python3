def inteiro_decimal(numero = 0):
    numero = float(input('Informe um número: '))
    arredondado = round(numero)
    if numero == arredondado:
        return f'{numero} é INTEIRO!'
    else:
        return f'{numero} é DECIMAL!'


print(inteiro_decimal())