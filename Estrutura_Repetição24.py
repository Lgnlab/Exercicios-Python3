def media_notas(notas = 0):
    soma = cont = 0
    while True:
        notas = int(input('Nota[999 para parar]: '))
        if notas == 999:
            break
        else:
            soma += notas
            cont += 1
    return f'Média das notas digitadas: {soma / cont}'


print(media_notas())