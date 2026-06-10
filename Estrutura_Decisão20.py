def par_impar(numero = 0):
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        return f'{numero} é PAR!'
    else:
        return f'{numero} é IMPAR!'
    

print(par_impar())