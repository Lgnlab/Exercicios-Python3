def notas(nota = 0):
    lista_media = []
    soma = 0
    contador = 1
    while contador < 11:
        print(f"Aluno {contador}:")
        for n in range(1, 5):
            nota = int(input("Nota: "))
            soma += nota
        media = soma / 4
        lista_media.append(media)
        soma = 0
        contador += 1
    print("Medias maiores ou igual a 7.0:")
    for m in lista_media:
        if m >= 7:
            print(f"{m:.1f}")

notas()