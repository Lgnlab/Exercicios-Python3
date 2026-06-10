def welcome(turno = '' ,msg = ''):
    try:
        turno = str(input('Turno(M, V, N): ')).upper().strip()[0]
        if turno == 'M':
            msg = 'Bom Dia!'
        elif turno == 'V':
            msg = 'Boa Tarde!'
        elif turno == 'N':
            msg = 'Boa Noite!'
        else:
            msg = 'Valor Inválido!'
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados.'
    else:
        return msg


print(welcome())