def notas(nota = 0):
    while True:
        nota = int(input('Informe a nota: '))
        if nota < 0 or nota > 10:
            print('Informe um valor válido!')
        else:
            break
    return f'Nota digitada: {nota}'


print(notas())
