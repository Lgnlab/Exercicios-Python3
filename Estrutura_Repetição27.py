def turma(turmas = 0, alunos = 0):
    turmas = int(input('Turmas: '))
    cont_alunos = 0
    cont_parada = 1
    while cont_parada <= turmas:
        alunos = int(input('Alunos: '))
        if alunos > 40:
            break
        else:
            cont_alunos += alunos
        cont_parada += 1
    return f'Média: {cont_alunos / turmas:.0f} alunos por turma'


print(turma())