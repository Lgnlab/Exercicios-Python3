def notas():
    lista_notas = []
    for cont in range(1, 5):
        lista_notas.append(int(input('Nota: ')))
    return f"Média final: {sum(lista_notas) / len(lista_notas):.1f}"

print(notas())