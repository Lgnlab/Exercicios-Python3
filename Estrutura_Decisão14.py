def notas(nota = 0):
    try:
        media = soma = 0
        for c in range(1, 3):
            nota = float(input(f'{c} Nota: '))
            soma += nota
        media = soma / 2
        if media >= 9 and media <= 10:
            msg = 'Conceito A - APROVADO'
        elif media >= 7.5:
            msg = 'Conceito B - APROVADO'
        elif media >= 6:
            msg = 'Conceito C - APROVADO'
        elif media >= 4:
            msg = 'Conceito D - REPROVADO'
        else:
            msg = 'Conceito E - REPROVADO'
    except (ValueError, TypeError):
        return 'Informe um número'
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados'
    else:
        return f'Média: {media:.1f}\n{msg}'
    

print(notas())