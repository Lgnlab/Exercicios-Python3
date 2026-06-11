def ginastica(nome = '', nota = 0):
    lista_notas = []
    nome = str(input("Atleta: ")).strip()
    for cont in range(1, 8):
        nota = float(input(f"Nota {cont}: "))
        lista_notas.append(nota)
    return f"Atleta: {nome}\nMelhor nota: {max(lista_notas)}\nPior nota: {min(lista_notas)}\nMédia: {sum(lista_notas) / len(lista_notas):.1f}"

print(ginastica())