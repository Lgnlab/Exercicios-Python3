def media_notas():
    controle = 1
    soma = 0
    while controle <= 4:
        nota = float(input(f'{controle} Nota: '))
        soma += nota
        controle += 1
    return f'Média: {soma / controle:.1f}'


resultado = media_notas()
print(resultado)