def ano_bissexto(ano = 0):
    bissexto = False
    ano = int(input('Ano: '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    return f'O ano de {ano} é BISSEXTO? {bissexto}'


print(ano_bissexto())
