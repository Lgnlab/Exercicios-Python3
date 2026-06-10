def voto(eleitores = 0, voto = 0):
    eleitores = int(input('Quantas pessoas vão votar? '))
    cont = 1
    candidato1 = candidato2 = candidato3 = 0
    while cont <= eleitores:
        voto = int(input('Voto[1/2/3]: '))
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        else:
            candidato3 += 1
        cont += 1
    return f'Apuração de votos:\nCanditado 1: {candidato1}\nCanditado 2: {candidato2}\nCanditado 3: {candidato3}'


print(voto())