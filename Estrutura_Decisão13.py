def dia_semana(numero = 0):
    numero = int(input('Informe um número: '))
    if numero == 1:
        dia = 'Domingo'
    elif numero == 2:
        dia = 'Segunda'
    elif numero == 3:
        dia = 'Terça'
    elif numero == 4:
        dia = 'Quarta'
    elif numero == 5:
        dia = 'Quinta'
    elif numero == 6:
        dia = 'Sexa'
    elif numero == 7:
        dia = 'Sábado'
    else:
        dia = 'Valor Inválido!'
    return dia


print(dia_semana())