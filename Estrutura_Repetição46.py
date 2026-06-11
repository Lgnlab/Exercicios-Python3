def saltos(nome = '', salto = 0):
    lista_saltos = []
    nome = str(input("Atleta: "))
    for cont in range(1, 6):
        salto = float(input(f"{cont} Salto: "))
        lista_saltos.append(salto)
    return f"Melhor salto: {max(lista_saltos)}\nPior salto: {min(lista_saltos)}\nMédia dos demais saltos: {sum(lista_saltos) / len(lista_saltos)}"


print(saltos())