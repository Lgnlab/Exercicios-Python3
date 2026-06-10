def media_nota(nota1 = 0, nota2 = 0):
    try:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
    except (TypeError, ValueError):
        print('Digite um valor válido.')
    except KeyboardInterrupt:
        print('Usuário preferiu não informar os dados.')
    else:
        media = (nota1 + nota2) / 2
        if media >= 7 and media <= 9:
            return f'Média: {media:.1f}\nAPROVADO!'
        elif media == 10:
            return f'Média: {media:.1f}\nAPROVADO COM DISTINÇÃO!'
        else:
            return f'Média: {media:.1f}\nREPROVADO!'
    return 'Até Breve.'

print(media_nota())