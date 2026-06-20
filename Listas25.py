def voto(enquete = int):
    from collections import Counter
    cont = 0
    lista_votos = []
    while True:
        enquete = int(input("Quem foi o melhor jogador[1-23]? "))
        if enquete > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
        elif enquete == 0:
            break
        else:
            lista_votos.append(enquete)
            cont += 1
    contagem_votos = Counter(lista_votos)

    dicionario_comun = dict(contagem_votos)

    print("Resultado da votação:")
    for k, v in dicionario_comun.items():
        perce = v / cont * 100
        print(f"Jogador: {k} - Votos: {v} - Percentual: {perce:.1f}%")


print(voto())